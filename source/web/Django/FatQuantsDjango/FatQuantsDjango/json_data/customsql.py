from ievv_opensource.ievv_customsql import customsql_registry


class JsonDataCustomSql(customsql_registry.AbstractCustomSql):
    def initialize(self):

        self.execute_sql("""
        
            -- ===============================================================
            -- Trigger function for json_data.created_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION json_data_created_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.created_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: json_data.created_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS created_timestamp_trigger ON json_data;
            CREATE TRIGGER created_timestamp_trigger
                AFTER INSERT ON json_data
                FOR EACH ROW
                EXECUTE PROCEDURE json_data_created_timestamp();


            -- ===============================================================
            -- Trigger function for json_data.updated_timestamp
            -- ===============================================================
            CREATE OR REPLACE FUNCTION json_data_updated_timestamp()
                RETURNS trigger AS
            $BODY$
            BEGIN
                NEW.updated_timestamp := current_timestamp;
                RETURN NULL;
            END;
            $BODY$
            LANGUAGE plpgsql;

            -- ---------------------------------------------------------------
            -- Trigger: json_data.updated_timestamp
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS updated_timestamp_trigger ON json_data;
            CREATE TRIGGER updated_timestamp_trigger
                AFTER UPDATE ON json_data
                FOR EACH ROW
                EXECUTE PROCEDURE json_data_updated_timestamp();

        """)

    def recreate_data(self):
        #self.execute_sql("""<NONE>""")
        pass

