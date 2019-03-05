from ievv_opensource.ievv_customsql import customsql_registry


class TickerCustomSql(customsql_registry.AbstractCustomSql):
    def initialize(self):

        self.execute_sql("""

            -- ===============================================================
            -- Trigger function for ticker.ticker_uuid generator
            -- ===============================================================
            CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
            CREATE OR REPLACE FUNCTION ticker_uuid_generator()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.ticker_uuid := uuid_generate_v4();
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: ticker table before_insert_trigger
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS before_insert_trigger ON ticker;
            CREATE TRIGGER before_insert_trigger
                BEFORE INSERT ON ticker
                FOR EACH ROW
                EXECUTE PROCEDURE ticker_uuid_generator();

        
            -- ---------------------------------------------------------------
            -- Trigger: ticker table
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON ticker;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON ticker
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();

        
            -- ---------------------------------------------------------------
            -- Trigger: ticker_identifier table
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON ticker_identifier;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON ticker_identifier
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();

        
            -- ---------------------------------------------------------------
            -- Trigger: ticker_market_index table
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON ticker_market_index;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON ticker_market_index
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: ticker_resource table
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON ticker_resource;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON ticker_resource
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ===============================================================
            -- Trigger function for ticker_batch_process.last_checked
            -- ===============================================================
            CREATE OR REPLACE FUNCTION ticker_batch_process_last_checked()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.last_checked := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: ticker_batch_process.last_checked
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS last_checked_trigger ON ticker_batch_process;
            CREATE TRIGGER last_checked_trigger
                BEFORE INSERT OR UPDATE ON ticker_batch_process
                FOR EACH ROW
                EXECUTE PROCEDURE ticker_batch_process_last_checked();


            -- ===============================================================
            -- Trigger function for ticker_eod_data.created_timestamp
            --
            -- NOTE: This will be used in early versions of the system.
            -- ===============================================================
            CREATE OR REPLACE FUNCTION ticker_eod_data_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: ticker_eod_data.created_timestamp
            --
            -- NOTE: This will be used in early versions of the system.
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON ticker_eod_data;
            CREATE TRIGGER created_timestamp_trigger
                BEFORE INSERT ON ticker_eod_data
                FOR EACH ROW
                EXECUTE PROCEDURE ticker_eod_data_created_timestamp();


            -- ===============================================================
            -- Trigger function for ticker_eod_data.updated_timestamp
            --
            -- NOTE: This will be used in early versions of the system.
            -- ===============================================================
            CREATE OR REPLACE FUNCTION ticker_eod_data_updated_timestamp()
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
            -- Trigger: ticker_eod_data.updated_timestamp
            --
            -- NOTE: This will be used in early versions of the system.
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS updated_timestamp_trigger ON ticker_eod_data;
            CREATE TRIGGER updated_timestamp_trigger
                BEFORE UPDATE ON ticker_eod_data
                FOR EACH ROW
                EXECUTE PROCEDURE ticker_eod_data_updated_timestamp();


            -- ===============================================================
            -- Trigger function for ticker_eod_data_audit_record table
            --
            -- This function implements a record-level audit trail.
            --
            -- NOTE: This will NOT be used in early versions of the system.
            -- ===============================================================
            /*
            CREATE OR REPLACE FUNCTION ticker_eod_data_audit_record_insert()
                RETURNS trigger AS
            $BODY$
            
            -- ---------------------------------------------------------------
            -- Declarations
            -- ---------------------------------------------------------------
            DECLARE

                -- -----------------------------------------------------------
                -- Audit Action
                -- -----------------------------------------------------------
                audit_action        smallint := NULL;
                audit_action_insert smallint := 1;
                audit_action_update smallint := 0;
                audit_action_delete smallint := -1;

                -- -----------------------------------------------------------
                -- Data field variables
                -- -----------------------------------------------------------
                ticker_eod_data_id  bigint;
                ticker_id           int;
                close_date          date;
                data_source         int;
                open_value          float8;
                high_value          float8;
                low_value           float8;
                close_value         float8;
                volume              float8;


            -- ---------------------------------------------------------------
            -- Trigger function
            -- ---------------------------------------------------------------
            BEGIN
                -- -----------------------------------------------------------
                -- Set the audit action
                -- -----------------------------------------------------------
                audit_action := NULL;

                -- -----------------------------------------------------------
                -- Insert
                -- -----------------------------------------------------------
                IF TG_OP = 'INSERT' THEN
                    audit_action       := audit_action_insert;
                    ticker_eod_data_id := NEW.ticker_eod_data_id;
                    ticker_id          := NEW.ticker_id;
                    close_date         := NEW.close_date;
                    data_source        := NEW.data_source;
                    open_value         := NEW.open_value;
                    high_value         := NEW.high_value;
                    low_value          := NEW.low_value;
                    close_value        := NEW.close_value;
                    volume             := NEW.volume;
                END IF;

                -- -----------------------------------------------------------
                -- Update: check whether the data has really changed
                -- -----------------------------------------------------------
                IF TG_OP = 'UPDATE' THEN

                    -- -------------------------------------------------------
                    -- ticker_eod_data_id
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.ticker_eod_data_id IS NULL) AND (NEW.ticker_eod_data_id IS NOT NULL) THEN
                            audit_action       := audit_action_update;
                            ticker_eod_data_id := NEW.ticker_eod_data_id;
                        END IF;
                        IF (OLD.ticker_eod_data_id IS NOT NULL) AND (NEW.ticker_eod_data_id IS NULL) THEN
                            audit_action       := audit_action_update;
                            ticker_eod_data_id := NEW.ticker_eod_data_id;
                        END IF;
                        IF (OLD.ticker_eod_data_id IS NOT NULL) AND (NEW.ticker_eod_data_id IS NOT NULL) AND (NEW.ticker_eod_data_id <> OLD.ticker_eod_data_id) THEN
                            audit_action       := audit_action_update;
                            ticker_eod_data_id := NEW.ticker_eod_data_id;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- ticker_id
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.ticker_id IS NULL) AND (NEW.ticker_id IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            ticker_id    := NEW.ticker_id;
                        END IF;
                        IF (OLD.ticker_id IS NOT NULL) AND (NEW.ticker_id IS NULL) THEN
                            audit_action := audit_action_update;
                            ticker_id    := NEW.ticker_id;
                        END IF;
                        IF (OLD.ticker_id IS NOT NULL) AND (NEW.ticker_id IS NOT NULL) AND (NEW.ticker_id <> OLD.ticker_id) THEN
                            audit_action := audit_action_update;
                            ticker_id    := NEW.ticker_id;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- close_date
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.close_date IS NULL) AND (NEW.close_date IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            close_date   := NEW.close_date;
                        END IF;
                        IF (OLD.close_date IS NOT NULL) AND (NEW.close_date IS NULL) THEN
                            audit_action := audit_action_update;
                            close_date   := NEW.close_date;
                        END IF;
                        IF (OLD.close_date IS NOT NULL) AND (NEW.close_date IS NOT NULL) AND (NEW.close_date <> OLD.close_date) THEN
                            audit_action := audit_action_update;
                            close_date   := NEW.close_date;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- data_source
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.data_source IS NULL) AND (NEW.data_source IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            data_source  := NEW.data_source;
                        END IF;
                        IF (OLD.data_source IS NOT NULL) AND (NEW.data_source IS NULL) THEN
                            audit_action := audit_action_update;
                            data_source  := NEW.data_source;
                        END IF;
                        IF (OLD.data_source IS NOT NULL) AND (NEW.data_source IS NOT NULL) AND (NEW.data_source <> OLD.data_source) THEN
                            audit_action := audit_action_update;
                            data_source  := NEW.data_source;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- open_value
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.open_value IS NULL) AND (NEW.open_value IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            open_value   := NEW.open_value;
                        END IF;
                        IF (OLD.open_value IS NOT NULL) AND (NEW.open_value IS NULL) THEN
                            audit_action := audit_action_update;
                            open_value   := NEW.open_value;
                        END IF;
                        IF (OLD.open_value IS NOT NULL) AND (NEW.open_value IS NOT NULL) AND (NEW.open_value <> OLD.open_value) THEN
                            audit_action := audit_action_update;
                            open_value   := NEW.open_value;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- high_value
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.high_value IS NULL) AND (NEW.high_value IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            high_value   := NEW.high_value;
                        END IF;
                        IF (OLD.high_value IS NOT NULL) AND (NEW.high_value IS NULL) THEN
                            audit_action := audit_action_update;
                            high_value   := NEW.high_value;
                        END IF;
                        IF (OLD.high_value IS NOT NULL) AND (NEW.high_value IS NOT NULL) AND (NEW.high_value <> OLD.high_value) THEN
                            audit_action := audit_action_update;
                            high_value   := NEW.high_value;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- low_value
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.low_value IS NULL) AND (NEW.low_value IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            low_value    := NEW.low_value;
                        END IF;
                        IF (OLD.low_value IS NOT NULL) AND (NEW.low_value IS NULL) THEN
                            audit_action := audit_action_update;
                            low_value    := NEW.low_value;
                        END IF;
                        IF (OLD.low_value IS NOT NULL) AND (NEW.low_value IS NOT NULL) AND (NEW.low_value <> OLD.low_value) THEN
                            audit_action := audit_action_update;
                            low_value    := NEW.low_value;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- close_value
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.close_value IS NULL) AND (NEW.close_value IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            close_value  := NEW.close_value;
                        END IF;
                        IF (OLD.close_value IS NOT NULL) AND (NEW.close_value IS NULL) THEN
                            audit_action := audit_action_update;
                            close_value  := NEW.close_value;
                        END IF;
                        IF (OLD.close_value IS NOT NULL) AND (NEW.close_value IS NOT NULL) AND (NEW.close_value <> OLD.close_value) THEN
                            audit_action := audit_action_update;
                            close_value  := NEW.close_value;
                        END IF;
                    END IF;

                    -- -------------------------------------------------------
                    -- volume
                    -- -------------------------------------------------------
                    IF (audit_action IS NULL) THEN
                        IF (OLD.volume IS NULL) AND (NEW.volume IS NOT NULL) THEN
                            audit_action := audit_action_update;
                            volume       := NEW.volume;
                        END IF;
                        IF (OLD.volume IS NOT NULL) AND (NEW.volume IS NULL) THEN
                            audit_action := audit_action_update;
                            volume       := NEW.volume;
                        END IF;
                        IF (OLD.volume IS NOT NULL) AND (NEW.volume IS NOT NULL) AND (NEW.volume <> OLD.volume) THEN
                            audit_action := audit_action_update;
                            volume       := NEW.volume;
                        END IF;
                    END IF;
                    
                END IF;

                -- -----------------------------------------------------------
                -- Delete
                -- -----------------------------------------------------------
                IF TG_OP = 'DELETE' THEN
                    audit_action       := audit_action_delete;
                    ticker_eod_data_id := OLD.ticker_eod_data_id;
                    ticker_id          := OLD.ticker_id;
                    close_date         := OLD.close_date;
                    data_source        := OLD.data_source;
                    open_value         := OLD.open_value;
                    high_value         := OLD.high_value;
                    low_value          := OLD.low_value;
                    close_value        := OLD.close_value;
                    volume             := OLD.volume;
                END IF;

                -- -----------------------------------------------------------
                -- Insert ticker_eod_data_audit_record entry if necessary
                -- -----------------------------------------------------------
                 IF (audit_action IS NOT NULL) THEN

                    -- -------------------------------------------------------
                    -- Insert ticker_eod_data_audit_record entry
                    -- -------------------------------------------------------
                        INSERT INTO ticker_eod_data_audit_record (
                            audit_action,
                            audit_timestamp,
                            ticker_eod_data_id,
                            ticker_id,
                            close_date,
                            data_source,
                            open_value,
                            high_value,
                            low_value,
                            close_value,
                            volume)
                        VALUES (
                            audit_action,
                            current_timestamp,
                            ticker_eod_data_id,
                            ticker_id,
                            close_date,
                            data_source,
                            open_value,
                            high_value,
                            low_value,
                            close_value,
                            volume);
                 END IF;

                -- -----------------------------------------------------------
                -- Return NULL (result ignored for AFTER trigger)
                -- -----------------------------------------------------------
                RETURN NULL;

            END;
            $BODY$
            LANGUAGE plpgsql;
            */


            -- ---------------------------------------------------------------
            -- Trigger: ticker_eod_data table
            --
            -- NOTE: This will NOT be used in early versions of the system.
            -- ---------------------------------------------------------------
            /*
            DROP TRIGGER IF EXISTS after_modification_trigger ON ticker_eod_data;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON ticker_eod_data
                FOR EACH ROW
                EXECUTE PROCEDURE ticker_eod_data_audit_record_insert();
            */

        """)

    def recreate_data(self):
        #self.execute_sql("""<NONE>""")
        pass

