from ievv_opensource.ievv_customsql import customsql_registry


class BatchProcessCustomSql(customsql_registry.AbstractCustomSql):
    def initialize(self):

        self.execute_sql("""
        
            -- ---------------------------------------------------------------
            -- Trigger: batch_process_type => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON batch_process_type;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON batch_process_type
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ===============================================================
            -- Trigger function for batch_process.created_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION batch_process_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: batch_process.created_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON batch_process;
            CREATE TRIGGER created_timestamp_trigger
                BEFORE INSERT ON batch_process
                FOR EACH ROW
                EXECUTE PROCEDURE batch_process_created_timestamp();


            -- ===============================================================
            -- Trigger function for batch_process.updated_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION batch_process_updated_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := OLD.created_timestamp;
                NEW.updated_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: batch_process.updated_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS updated_timestamp_trigger ON batch_process;
            CREATE TRIGGER updated_timestamp_trigger
                BEFORE UPDATE ON batch_process
                FOR EACH ROW
                EXECUTE PROCEDURE batch_process_updated_timestamp();


            -- ===============================================================
            -- Trigger function for batch_process_log.log_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION batch_process_log_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.log_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: batch_process_log.log_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS log_timestamp_trigger ON batch_process_log;
            CREATE TRIGGER log_timestamp_trigger
                BEFORE INSERT ON batch_process_log
                FOR EACH ROW
                EXECUTE PROCEDURE batch_process_log_timestamp();


            -- ===============================================================
            -- Trigger function for batch_process_task.created_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION batch_process_task_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: batch_process_task.created_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON batch_process_task;
            CREATE TRIGGER created_timestamp_trigger
                BEFORE INSERT ON batch_process_task
                FOR EACH ROW
                EXECUTE PROCEDURE batch_process_task_created_timestamp();


            -- ===============================================================
            -- Trigger function for batch_process_task.updated_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION batch_process_task_updated_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := OLD.created_timestamp;
                NEW.updated_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: batch_process_task.updated_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS updated_timestamp_trigger ON batch_process_task;
            CREATE TRIGGER updated_timestamp_trigger
                BEFORE UPDATE ON batch_process_task
                FOR EACH ROW
                EXECUTE PROCEDURE batch_process_task_updated_timestamp();


            -- ===============================================================
            -- Trigger function for batch_process_task_intervention.intervention_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION batch_process_task_intervention_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.intervention_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: batch_process_task_intervention.intervention_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS intervention_timestamp_trigger ON batch_process_task_intervention;
            CREATE TRIGGER intervention_timestamp_trigger
                BEFORE INSERT OR UPDATE ON batch_process_task_intervention
                FOR EACH ROW
                EXECUTE PROCEDURE batch_process_task_intervention_timestamp();

        """)

    def recreate_data(self):
        #self.execute_sql("""<NONE>""")
        pass
