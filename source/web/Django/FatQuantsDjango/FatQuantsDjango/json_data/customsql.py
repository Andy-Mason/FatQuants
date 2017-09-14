from ievv_opensource.ievv_customsql import customsql_registry


class JSONDataCustomSql(customsql_registry.AbstractCustomSql):
    def initialize(self):

        self.execute_sql("""
        
            -- ---------------------------------------------------------------
            -- Trigger: json_data_set_type => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON json_data_set_type;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON json_data_set_type
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ===============================================================
            -- Trigger function for json_data_set.created_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION json_data_set_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: json_data_set.created_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON json_data_set;
            CREATE TRIGGER created_timestamp_trigger
                AFTER INSERT ON json_data_set
                FOR EACH ROW
                EXECUTE PROCEDURE json_data_set_created_timestamp();


            -- ===============================================================
            -- Trigger function for json_data_set.updated_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION json_data_set_updated_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.updated_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: json_data_set.updated_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS updated_timestamp_trigger ON json_data_set;
            CREATE TRIGGER updated_timestamp_trigger
                AFTER UPDATE ON json_data_set
                FOR EACH ROW
                EXECUTE PROCEDURE json_data_set_updated_timestamp();


            -- ===============================================================
            -- Trigger function for json_data_item.created_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION json_data_item_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: json_data_item.created_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON json_data_item;
            CREATE TRIGGER created_timestamp_trigger
                AFTER INSERT ON json_data_item
                FOR EACH ROW
                EXECUTE PROCEDURE json_data_item_created_timestamp();


            -- ===============================================================
            -- Trigger function for json_data_item.updated_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION json_data_item_updated_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.updated_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: json_data_item.updated_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS updated_timestamp_trigger ON json_data_item;
            CREATE TRIGGER updated_timestamp_trigger
                AFTER UPDATE ON json_data_item
                FOR EACH ROW
                EXECUTE PROCEDURE json_data_item_updated_timestamp();

        """)

    def recreate_data(self):
        #self.execute_sql("""<NONE>""")
        pass

