from ievv_opensource.ievv_customsql import customsql_registry


class ProcessCustomSql(customsql_registry.AbstractCustomSql):
    def initialize(self):

        self.execute_sql("""
        
            -- ---------------------------------------------------------------
            -- Trigger: process_type => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON process_type;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON process_type
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: process_type_json_data_set_type => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON process_type_json_data_set_type;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON process_type_json_data_set_type
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ===============================================================
            -- Trigger function for process.created_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION process_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: process.created_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON process;
            CREATE TRIGGER created_timestamp_trigger
                AFTER INSERT ON process
                FOR EACH ROW
                EXECUTE PROCEDURE process_created_timestamp();


            -- ===============================================================
            -- Trigger function for process.updated_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION process_updated_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.updated_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: process.updated_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS updated_timestamp_trigger ON process;
            CREATE TRIGGER updated_timestamp_trigger
                AFTER UPDATE ON process
                FOR EACH ROW
                EXECUTE PROCEDURE process_updated_timestamp();


            -- ===============================================================
            -- Trigger function for process_json_data_set.created_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION process_json_data_set_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: process_json_data_set.created_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON process_json_data_set;
            CREATE TRIGGER created_timestamp_trigger
                AFTER INSERT ON process_json_data_set
                FOR EACH ROW
                EXECUTE PROCEDURE process_json_data_set_created_timestamp();


            -- ===============================================================
            -- Trigger function for process_log.log_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION process_log_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.log_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: process_log.log_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS log_timestamp_trigger ON process_log;
            CREATE TRIGGER log_timestamp_trigger
                AFTER INSERT OR UPDATE ON process_log
                FOR EACH ROW
                EXECUTE PROCEDURE process_log_timestamp();

        """)

    def recreate_data(self):
        #self.execute_sql("""<NONE>""")
        pass

