from ievv_opensource.ievv_customsql import customsql_registry


class SystemCustomSql(customsql_registry.AbstractCustomSql):
    def initialize(self):

        self.execute_sql("""
        
            -- ===============================================================
            -- Trigger function for system_audit_record table
            --
            -- This function implements a field-level audit trail.
            -- ===============================================================
            CREATE OR REPLACE FUNCTION system_audit_record_insert()
                RETURNS trigger AS
            $BODY$
            
            -- ---------------------------------------------------------------
            -- Declarations
            -- ---------------------------------------------------------------
            DECLARE

                -- -----------------------------------------------------------
                -- Audit Action
                -- -----------------------------------------------------------
                audit_action        smallint    := NULL;
                audit_action_insert smallint    := 1;
                audit_action_update smallint    := 0;
                audit_action_delete smallint    := -1;
                audit_timestamp     timestamptz := current_timestamp;

                -- -----------------------------------------------------------
                -- Primary key variables
                -- -----------------------------------------------------------
                primary_key_field        varchar := NULL;
                primary_key_field_name   varchar := NULL;
                primary_key_field_value  int8    := NULL;

                -- -----------------------------------------------------------
                -- System Data Types
                -- -----------------------------------------------------------
                datatype_boolean     smallint := 1;
                datatype_integer     smallint := 2;
                datatype_float       smallint := 3;
                datatype_decimal     smallint := 4;
                datatype_date        smallint := 5;
                datatype_time        smallint := 6;
                datatype_datetime    smallint := 7;
                datatype_duration    smallint := 8;
                datatype_text        smallint := 9;
                datatype_json        smallint := 10;
                datatype_blob        smallint := 11;

                -- -----------------------------------------------------------
                -- Data Value variables
                -- -----------------------------------------------------------
                value_boolean    bool;
                value_integer    int8;
                value_float      float8;
                value_decimal    numeric;
                value_date       date;
                value_time       time;
                value_datetime   timestamptz;
                value_duration   interval;
                value_text       text;
                value_json       jsonb;
                value_blob       bytea;

                -- -----------------------------------------------------------
                -- Local variables
                -- ### TODO: Will old_value/new_value text work with bytea data?
                -- -----------------------------------------------------------
                table_field      record;
                field_datatype   smallint;
                field_value_old  text;
                field_value_new  text;


            -- ---------------------------------------------------------------
            -- Trigger function
            -- ---------------------------------------------------------------
            BEGIN
                -- -----------------------------------------------------------
                -- Iterate through the primary key fields
                -- -----------------------------------------------------------
                -- IMPLEMENTATION NOTE:
                -- In this application we must have exactly one primary key
                -- field. No primary key or a composite primary key is not
                -- allowed. An exception is raised if this rule is breached.
                --
                -- Furthermore, the primary key must be of integer type that
                -- can be cast to an int8 type.
                --
                -- We cannot use the information_schema to get the 
                -- primary key field. The constraint_column_usage view
                -- returns no rows if the user is not the dbowner.
                -- So we need to use the pg_* views instead.
                -- -----------------------------------------------------------
                primary_key_field_name  := NULL;
                primary_key_field_value := NULL;

                /* ### OLD QUERY USING information_schema ####################
                FOR primary_key_field IN
                SELECT information_schema.constraint_column_usage.column_name
                FROM information_schema.constraint_column_usage
                INNER JOIN information_schema.table_constraints
                USING (constraint_catalog, constraint_schema, constraint_name, table_catalog, table_schema, table_name)
                WHERE information_schema.table_constraints.constraint_type = 'PRIMARY KEY'
                  AND information_schema.table_constraints.table_schema = quote_ident(TG_TABLE_SCHEMA)
                  AND information_schema.table_constraints.table_name = quote_ident(TG_TABLE_NAME)
                ########################################################### */

                -- -----------------------------------------------------------
                -- NEW QUERY USING pg_* views
                -- -----------------------------------------------------------
                FOR primary_key_field IN

                SELECT pg_attribute.attname FROM pg_index
                INNER JOIN  pg_attribute 
                  ON  pg_attribute.attrelid = pg_index.indrelid
                  AND pg_attribute.attnum = ANY(pg_index.indkey)
                INNER JOIN pg_class 
                  ON (pg_attribute.attrelid = pg_class.oid)
                INNER JOIN pg_namespace
                  ON (pg_namespace.oid = pg_class.relnamespace)   
                WHERE pg_namespace.nspname = quote_ident(TG_TABLE_SCHEMA)
                  AND pg_class.relname = quote_ident(TG_TABLE_NAME)
                  AND pg_index.indisprimary

                LOOP
                    -- -------------------------------------------------------
                    -- Check whether primary key data has already been set
                    -- -------------------------------------------------------
                    IF primary_key_field_name IS NOT NULL THEN
                        RAISE EXCEPTION 'Table: ''%'' has more than one Primary Key Field. This use case is not handled.', quote_ident(TG_TABLE_NAME)
                        USING HINT = '(Implementation Restriction Violation)';
                    END IF;

                    -- -------------------------------------------------------
                    -- Set the primary key data 
                    -- -------------------------------------------------------
                    primary_key_field_name := primary_key_field;
                    IF TG_OP = 'INSERT' THEN
                        EXECUTE
                          'SELECT ($1).' || primary_key_field_name || '::int8'
                          USING NEW INTO primary_key_field_value;
                    ELSE
                        EXECUTE
                          'SELECT ($1).' || primary_key_field_name || '::int8'
                          USING OLD INTO primary_key_field_value;
                    END IF;

                END LOOP;
                -- -----------------------------------------------------------
                -- END OF: Iterate through the primary key fields
                -- -----------------------------------------------------------

                -- -----------------------------------------------------------
                -- Check whether we have primary key data
                -- -----------------------------------------------------------
                IF primary_key_field_name IS NULL THEN
                    RAISE EXCEPTION 'Table: ''%'' has no Primary Key Field. This use case is not handled.', quote_ident(TG_TABLE_NAME)
                    USING HINT = '(Implementation Restriction Violation)';
                END IF;


                -- -----------------------------------------------------------
                -- Iterate through table fields
                -- -----------------------------------------------------------
                -- IMPLEMENTATION NOTE:
                -- This query uses the information_schema views.
                -- This does not work if the user only has SELECT privileges.
                -- That works for this application because a user only having
                -- SELECT privileges cannot modify table data and hence will
                -- not be adding records to the system_audit_record table.
                --
                -- An application which requires access to information_schema
                -- data for users only having SELECT privileges should use 
                -- the pg_* views instead.
                -- -----------------------------------------------------------
                FOR table_field IN

	            SELECT
                   information_schema.columns.column_name, 
                   information_schema.columns.udt_name
	            FROM information_schema.columns
	            WHERE table_schema = quote_ident(TG_TABLE_SCHEMA)
	              AND table_name = quote_ident(TG_TABLE_NAME)
	            ORDER BY information_schema.columns.ordinal_position

                /* ### ALTERNATIVE QUERY USING pg_* views ####################
                SELECT 
                   pg_attribute.attname AS column_name,
                   pg_type.typname AS udt_name
                FROM pg_attribute
                INNER JOIN pg_type 
                   ON pg_type.oid = pg_attribute.atttypid
                WHERE pg_attribute.attnum > 0
                  AND NOT pg_attribute.attisdropped
                  AND pg_attribute.attrelid = (
                        SELECT pg_class.oid
                        FROM pg_class
                        LEFT JOIN pg_catalog.pg_namespace AS pg_namespace 
                          ON pg_namespace.oid = pg_class.relnamespace
                        WHERE pg_namespace.nspname = quote_ident(TG_TABLE_SCHEMA)
	                      AND pg_class.relname = quote_ident(TG_TABLE_NAME)
                          AND pg_table_is_visible(pg_class.oid)
                      )
                ORDER BY pg_attribute.attnum
                ########################################################### */

                LOOP
                    -- -------------------------------------------------------
                    -- Set the field datatype
                    -- -------------------------------------------------------
                    -- IMPLEMENTATION NOTE:
                    -- This mapping used to be in a system_data_type_mapping 
                    -- table. This is potentially dangerous because the
                    -- mapping entries could be modified by a malicious
                    -- process or by a well-intentioned but uninformed user.
                    -- It is therefore safer to hard-code the mapping here.
                    -- Execution speed should also be faster too.
                    -- -------------------------------------------------------
                    field_datatype := NULL;

                    IF table_field.udt_name = 'bool' THEN
                        field_datatype := datatype_boolean;
                    END IF;

                    IF table_field.udt_name = 'int2' THEN
                        field_datatype := datatype_integer;
                    END IF;

                    IF table_field.udt_name = 'int4' THEN
                        field_datatype := datatype_integer;
                    END IF;

                    IF table_field.udt_name = 'int8' THEN
                        field_datatype := datatype_integer;
                    END IF;

                    IF table_field.udt_name = 'float8' THEN
                        field_datatype := datatype_float;
                    END IF;

                    IF table_field.udt_name = 'numeric' THEN
                        field_datatype := datatype_decimal;
                    END IF;

                    IF table_field.udt_name = 'date' THEN
                        field_datatype := datatype_date;
                    END IF;

                    IF table_field.udt_name = 'time' THEN
                        field_datatype := datatype_time;
                    END IF;

                    IF table_field.udt_name = 'timestamptz' THEN
                        field_datatype := datatype_datetime;
                    END IF;

                    IF table_field.udt_name = 'interval' THEN
                        field_datatype := datatype_duration;
                    END IF;

                    IF table_field.udt_name = 'inet' THEN
                        field_datatype := datatype_text;
                    END IF;

                    IF table_field.udt_name = 'text' THEN
                        field_datatype := datatype_text;
                    END IF;

                    IF table_field.udt_name = 'uuid' THEN
                        field_datatype := datatype_text;
                    END IF;

                    IF table_field.udt_name = 'varchar' THEN
                        field_datatype := datatype_text;
                    END IF;

                    IF table_field.udt_name = 'jsonb' THEN
                        field_datatype := datatype_json;
                    END IF;

                    IF table_field.udt_name = 'bytea' THEN
                        field_datatype := datatype_blob;
                    END IF;


                    -- -------------------------------------------------------
                    -- Check for missing udt_name => field_datatype mapping
                    -- -------------------------------------------------------
                    IF (field_datatype IS NULL) THEN
                        RAISE EXCEPTION 'No field datatype mapping for: ''%'' in system_audit_record_insert().', table_field.udt_name
                        USING HINT = '(Unmapped table_field.udt_name)';
                    END IF;


                    -- -------------------------------------------------------
                    -- Set the audit action
                    -- -------------------------------------------------------
                    audit_action := NULL;

                    IF TG_OP = 'INSERT' THEN
                        EXECUTE
                          'SELECT ($1).' || table_field.column_name || '::text'
                          USING NEW INTO field_value_new;

                        IF (field_value_new IS NOT NULL) THEN
                            audit_action := audit_action_insert;  
                        END IF;
                    END IF;

                    IF TG_OP = 'UPDATE' THEN
                        EXECUTE
                          'SELECT ($1).' || table_field.column_name || '::text'
                          USING OLD INTO field_value_old;

                        EXECUTE
                          'SELECT ($1).' || table_field.column_name || '::text'
                          USING NEW INTO field_value_new;

                        IF (field_value_old IS NULL) AND (field_value_new IS NOT NULL) THEN
                            audit_action := audit_action_update;  
                        END IF;

                        IF (field_value_old IS NOT NULL) AND (field_value_new IS NULL) THEN
                            audit_action := audit_action_update;  
                        END IF;

                        IF (field_value_old IS NOT NULL) AND (field_value_new IS NOT NULL) AND (field_value_new <> field_value_old) THEN
                            audit_action := audit_action_update;  
                        END IF;
                    END IF;

                    IF TG_OP = 'DELETE' THEN
                        EXECUTE
                          'SELECT ($1).' || table_field.column_name || '::text'
                          USING OLD INTO field_value_old;

                        IF (field_value_old IS NOT NULL) THEN
                            audit_action := audit_action_delete;  
                        END IF;
                    END IF;


                    -- -------------------------------------------------------
                    -- Insert system_audit_record entry if necessary
                    -- -------------------------------------------------------
                    IF (audit_action IS NOT NULL) THEN

                        -- ---------------------------------------------------
                        -- Get the field value
                        -- ---------------------------------------------------
                        value_boolean    := NULL;
                        value_integer    := NULL;
                        value_float      := NULL;
                        value_decimal    := NULL;
                        value_date       := NULL;
                        value_time       := NULL;
                        value_datetime   := NULL;
                        value_duration   := NULL;
                        value_text       := NULL;
                        value_json       := NULL;
                        value_blob       := NULL;

                        -- ---------------------------------------------------
                        -- Boolean
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_boolean THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_boolean;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_boolean;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- Integer
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_integer THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_integer;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_integer;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- Float
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_float THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_float;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_float;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- Decimal
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_decimal THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_decimal;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_decimal;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- Date
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_date THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_date;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_date;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- Time
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_time THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_time;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_time;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- DateTime
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_datetime THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_datetime;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_datetime;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- Duration
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_duration THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_duration;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_duration;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- Text
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_text THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name || '::text'
                                  USING OLD INTO value_text;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name || '::text'
                                  USING NEW INTO value_text;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- JSON
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_json THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_json;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_json;
                            END IF;
                        END IF;

                        -- ---------------------------------------------------
                        -- BLOB
                        -- ---------------------------------------------------
                        IF field_datatype = datatype_blob THEN
                            IF TG_OP = 'DELETE' THEN
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING OLD INTO value_blob;
                            ELSE
                                EXECUTE
                                  'SELECT ($1).' || table_field.column_name
                                  USING NEW INTO value_blob;
                            END IF;
                        END IF;


                        -- ---------------------------------------------------
                        -- Set audit_timestamp to the current_timestamp
                        -- ---------------------------------------------------
                        audit_timestamp := current_timestamp;


                        -- ---------------------------------------------------
                        -- Insert system_audit_record entry
                        -- ---------------------------------------------------
                        INSERT INTO system_audit_record (
                            audit_action,
                            audit_timestamp,
                            table_name,
                            primary_key_field_name,
                            primary_key_field_value,
                            field_name,
                            field_data_type,
                            field_value_boolean,
                            field_value_integer,
                            field_value_float,
                            field_value_decimal,
                            field_value_date,
                            field_value_time,
                            field_value_datetime,
                            field_value_duration,
                            field_value_text,
                            field_value_json,
                            field_value_blob)
                        VALUES (
                            audit_action,
                            audit_timestamp,
                            TG_TABLE_NAME,
                            primary_key_field_name,
                            primary_key_field_value,
                            table_field.column_name,
                            field_datatype,
                            value_boolean,
                            value_integer,
                            value_float,
                            value_decimal,
                            value_date,
                            value_time,
                            value_datetime,
                            value_duration,
                            value_text,
                            value_json,
                            value_blob);

                    END IF;
                    -- -------------------------------------------------------
                    -- END OF: Insert system_audit_record entry if necessary
                    -- -------------------------------------------------------

                END LOOP;
                -- -----------------------------------------------------------
                -- END OF: Iterate through table fields
                -- -----------------------------------------------------------


                -- -----------------------------------------------------------
                -- Return NULL (result ignored for AFTER trigger)
                -- -----------------------------------------------------------
                RETURN NULL;

            END;
            $BODY$
            LANGUAGE plpgsql;

        """)

    def recreate_data(self):
        #self.execute_sql("""<NONE>""")
        pass

