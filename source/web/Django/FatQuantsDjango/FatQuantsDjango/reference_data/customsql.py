from ievv_opensource.ievv_customsql import customsql_registry


class RefDataCustomSql(customsql_registry.AbstractCustomSql):
    def initialize(self):

        self.execute_sql("""
        
            -- ---------------------------------------------------------------
            -- Trigger: refdata_country => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON refdata_country;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON refdata_country
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: refdata_currency => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON refdata_currency;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON refdata_currency
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: refdata_identifier_type => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON refdata_identifier_type;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON refdata_identifier_type
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: refdata_market_index => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON refdata_market_index;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON refdata_market_index
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: refdata_resource_type => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON refdata_resource_type;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON refdata_resource_type
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: refdata_test => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON refdata_test;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON refdata_test
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();


            -- ---------------------------------------------------------------
            -- Trigger: refdata_trading_exchange => system_audit_record
            -- ---------------------------------------------------------------
            DROP TRIGGER IF EXISTS after_modification_trigger ON refdata_trading_exchange;
            CREATE TRIGGER after_modification_trigger
                AFTER INSERT OR UPDATE OR DELETE ON refdata_trading_exchange
                FOR EACH ROW
                EXECUTE PROCEDURE system_audit_record_insert();

        """)

    def recreate_data(self):
        #self.execute_sql("""<NONE>""")
        pass

