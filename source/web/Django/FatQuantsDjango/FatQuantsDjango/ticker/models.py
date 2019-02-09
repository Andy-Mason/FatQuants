from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

from datetime import date
import uuid


#-----------------------------------------------------------------------------
# Ticker
#-----------------------------------------------------------------------------
class Ticker(models.Model):

    ticker_id = \
        models.BigAutoField(verbose_name='TickerID',
                            db_column='ticker_id',
                            primary_key=True)

    ticker_uuid = \
        models.UUIDField(verbose_name='TickerUUID',
                         db_column='ticker_uuid',
                         unique=True,
                         default=uuid.uuid4,
                         null=False,
                         editable=False)

    #-------------------------------------------------------------------------
    # TICKER_STATUS TYPES
    #-------------------------------------------------------------------------
    TICKER_STATUS_INACTIVE = -1
    TICKER_STATUS_STALE    = 0
    TICKER_STATUS_ACTIVE   = 1
    TICKER_STATUS__TYPES = ( 
        (TICKER_STATUS_INACTIVE, 'InActive'), 
        (TICKER_STATUS_STALE,    'Stale'), 
        (TICKER_STATUS_ACTIVE,   'Active')
    )    
    status = \
        models.SmallIntegerField(verbose_name='Status',
                                 db_column='status',
                                 choices=TICKER_STATUS__TYPES,
                                 default=TICKER_STATUS_STALE,
                                 null=False,
                                 blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=200,
                         default='',
                         null=False,
                         blank=False)

    issuer_name = \
        models.CharField(verbose_name='Issuer Name',
                         db_column='issuer_name',
                         max_length=100,
                         default='',
                         null=False,
                         blank=True)

    security_name = \
        models.CharField(verbose_name='Security Name',
                         db_column='security_name',
                         max_length=100,
                         default='',
                         null=False,
                         blank=True)

    #-------------------------------------------------------------------------
    # INSTRUMENT_MODEL TYPES
    #-------------------------------------------------------------------------
    INSTRUMENT_MODEL_NONE      = 0
    INSTRUMENT_MODEL_COMMODITY = 1
    INSTRUMENT_MODEL_FX        = 2
    INSTRUMENT_MODEL_INDEX     = 3
    INSTRUMENT_MODEL_BOND      = 4
    INSTRUMENT_MODEL_SHARE     = 5
    INSTRUMENT_MODEL_INVTRUST  = 6
    INSTRUMENT_MODEL_ETP       = 7
    INSTRUMENT_MODEL_FUND      = 8
    INSTRUMENT_MODEL__TYPES = ( 
        (INSTRUMENT_MODEL_NONE,      '<None>'), 
        (INSTRUMENT_MODEL_COMMODITY, 'Commodity'), 
        (INSTRUMENT_MODEL_FX,        'FX'),
        (INSTRUMENT_MODEL_INDEX,     'Index'),
        (INSTRUMENT_MODEL_BOND,      'Bond'),
        (INSTRUMENT_MODEL_SHARE,     'Share'),
        (INSTRUMENT_MODEL_INVTRUST,  'InvestmentTrust'),
        (INSTRUMENT_MODEL_ETP,       'ETP'),
        (INSTRUMENT_MODEL_FUND,      'Fund')
    )    
    instrument_model = \
        models.SmallIntegerField(verbose_name='Instrument Model',
                                 db_column='instrument_model',
                                 choices=INSTRUMENT_MODEL__TYPES,
                                 default=INSTRUMENT_MODEL_NONE,
                                 null=False,
                                 blank=False)

    instrument_type = \
        models.CharField(verbose_name='Instrument Type',
                         db_column='instrument_type',
                         max_length=30,
                         default='',
                         null=False,
                         blank=True)
    
    instrument_subtype = \
        models.CharField(verbose_name='Instrument Subtype',
                         db_column='instrument_subtype',
                         max_length=30,
                         default='',
                         null=False,
                         blank=True)
    
    product_provider_id = \
        models.ForeignKey('reference_data.ProductProvider',
                          on_delete=models.PROTECT,
                          verbose_name='Product Provider',
                          db_column='product_provider_id',
                          null=True,
                          blank=True)
    
    product_leverage = \
        models.FloatField(verbose_name='Product Leverage',
                          db_column='product_leverage',
                          null=True,
                          blank=True)
    
    #-------------------------------------------------------------------------
    # FUND_UNIT_TYPES
    #-------------------------------------------------------------------------
    FUND_UNIT_ACCUMULATION = 'Acc'
    FUND_UNIT_INCOME = 'Inc'
    FUND_UNIT__TYPES = ( 
        (FUND_UNIT_ACCUMULATION, 'Accumulation'), 
        (FUND_UNIT_INCOME, 'Income') 
    )
    unit_type = \
        models.CharField(verbose_name='Unit Type',
                         db_column='unit_type',
                         max_length=3,
                         choices=FUND_UNIT__TYPES,
                         default='',
                         null=False,
                         blank=True)
    
    registered_country_id = \
        models.ForeignKey('reference_data.Country',
                          on_delete=models.PROTECT,
                          verbose_name='Registered Country',
                          db_column='registered_country_id',
                          null=True,
                          blank=True)
    
    issue_size = \
        models.FloatField(verbose_name='Issue Size',
                          db_column='issue_size',
                          null=True,
                          blank=True)
    
    quote_units = \
        models.FloatField(verbose_name='Quote Units',
                          db_column='quote_units',
                          null=True,
                          blank=True)

    quote_currency_id = \
        models.ForeignKey('reference_data.Currency',
                          on_delete=models.PROTECT,
                          related_name='quote_currency',
                          verbose_name='Quote Currency',
                          db_column='quote_currency_id',
                          null=True,
                          blank=True)
    
    trading_currency_id = \
        models.ForeignKey('reference_data.Currency',
                          on_delete=models.PROTECT,
                          related_name='trading_currency',
                          verbose_name='Trading Currency',
                          db_column='trading_currency_id',
                          null=True,
                          blank=True)
    
    trading_exchange_id = \
        models.ForeignKey('reference_data.TradingExchange',
                          on_delete=models.PROTECT,
                          verbose_name='Trading Exchange',
                          db_column='trading_exchange_id',
                          null=True,
                          blank=True)
    
    listing_type = \
        models.CharField(verbose_name='Listing Type',
                         db_column='listing_type',
                         max_length=20,
                         default='',
                         null=False,
                         blank=True)
    
    listing_code = \
        models.CharField(verbose_name='Listing Code',
                         db_column='listing_code',
                         max_length=20,
                         default='',
                         null=False,
                         blank=True)
    
    
    listing_category = \
        models.CharField(verbose_name='Listing Category',
                         db_column='listing_category',
                         max_length=60,
                         default='',
                         null=False,
                         blank=True)
    listing_date = \
        models.DateField(verbose_name='Listing Date',
                         db_column='listing_date',
                         null=True,
                         blank=True)
    
    exchange_market_size = \
        models.FloatField(verbose_name='Exchange Market Size',
                          db_column='exchange_market_size',
                          null=True,
                          blank=True)

    trading_service = \
        models.CharField(verbose_name='Trading Service',
                         db_column='trading_service',
                         max_length=60,
                         default='',
                         null=False,
                         blank=True)
    
    trading_segment = \
        models.CharField(verbose_name='Trading Segment',
                         db_column='trading_segment',
                         max_length=20,
                         default='',
                         null=False,
                         blank=True)
    
    market_sector_id = \
        models.ForeignKey('reference_data.MarketSector',
                          on_delete=models.PROTECT,
                          related_name='market_sector',
                          verbose_name='Market Sector',
                          db_column='market_sector_id',
                          null=True,
                          blank=True)
    
    morningstar_category_id = \
        models.ForeignKey('reference_data.MarketSector',
                          on_delete=models.PROTECT,
                          related_name='morningstar_category',
                          verbose_name='Morningstar Category',
                          db_column='morningstar_category_id',
                          null=True,
                          blank=True)
    
    json_data = \
        JSONField(verbose_name='JSON Data',
                  db_column='json_data',
                  null=True,
                  blank=True)

    class Meta:
        db_table = 'ticker'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# TickerIdentifier
#-----------------------------------------------------------------------------
class TickerIdentifier(models.Model):

    id = \
        models.BigAutoField(verbose_name='ID',
                            db_column='id',
                            primary_key=True)

    ticker_id = \
        models.ForeignKey(Ticker,
                          on_delete=models.CASCADE,
                          verbose_name='TickerID',
                          db_column='ticker_id',
                          default=0,
                          null=False,
                          blank=False)
    
    identifier_type_id = \
        models.ForeignKey('reference_data.IdentifierType',
                          on_delete=models.PROTECT,
                          verbose_name='Identifier Type',
                          db_column='identifier_type_id',
                          default=0,
                          null=False,
                          blank=False)
    
    identifier_code = \
        models.CharField(verbose_name='Identifier Code',
                         db_column='identifier_code',
                         max_length=40,
                         default='',
                         null=False,
                         blank=False)

    class Meta:
        db_table = 'ticker_identifier'
        unique_together = ('ticker_id', 'identifier_type_id')

    def __str__(self): 
        return self.name


#-----------------------------------------------------------------------------
# TickerMarketIndex
#-----------------------------------------------------------------------------
class TickerMarketIndex(models.Model):

    id = \
        models.BigAutoField(verbose_name='ID',
                            db_column='id',
                            primary_key=True)

    ticker_id = \
        models.ForeignKey(Ticker,
                          on_delete=models.CASCADE,
                          verbose_name='TickerID',
                          db_column='ticker_id',
                          default=0,
                          null=False,
                          blank=False)
        
    market_index_id = \
        models.ForeignKey('reference_data.MarketIndex',
                          on_delete=models.PROTECT,
                          verbose_name='MarketIndexID',
                          db_column='market_index_id',
                          default=0,
                          null=False,
                          blank=False)
    
    class Meta:
        db_table = 'ticker_market_index'
        unique_together = ('ticker_id', 'market_index_id')

    def __str__(self): 
        return self.name


#-----------------------------------------------------------------------------
# TickerResource
#-----------------------------------------------------------------------------
class TickerResource(models.Model):

    id = \
        models.BigAutoField(verbose_name='ID',
                            db_column='id',
                            primary_key=True)
    
    ticker_id = \
        models.ForeignKey(Ticker,
                          on_delete=models.CASCADE,
                          verbose_name='TickerID',
                          db_column='ticker_id',
                          default=0,
                          null=False,
                          blank=False)
    
    #-------------------------------------------------------------------------
    # RESOURCE TYPES
    #-------------------------------------------------------------------------
    RESOURCE_NONE            = 0
    RESOURCE_COMPANY_WEBSITE = 1
    RESOURCE_LSE_WEBPAGE     = 2
    RESOURCE_AJBELL_WEBPAGE  = 3
    RESOURCE__TYPES = ( 
        (RESOURCE_NONE,            '<None>'), 
        (RESOURCE_COMPANY_WEBSITE, 'Company website'), 
        (RESOURCE_LSE_WEBPAGE,     'London Stock Exchange web page'),
        (RESOURCE_AJBELL_WEBPAGE,  'AJ Bell web page')
    )    
    resource_type = \
        models.SmallIntegerField(verbose_name='Resource Type',
                                 db_column='resource_type',
                                 choices=RESOURCE__TYPES,
                                 default=RESOURCE_NONE,
                                 null=False,
                                 blank=False)
    
    resource_url = \
        models.URLField(verbose_name='Resource',
                        db_column='resource',
                        max_length=2000,
                        default='',
                        null=False,
                        blank=False)
    
    class Meta:
        db_table = 'ticker_resource'
        unique_together = ('ticker_id', 'resource_type')

    def __str__(self): 
        return self.name


#-----------------------------------------------------------------------------
# TickerEodData
#-----------------------------------------------------------------------------
class TickerEodData(models.Model):

    ticker_eod_data_id = \
        models.BigAutoField(verbose_name='TickerEodDataID',
                            db_column='ticker_eod_data_id',
                            primary_key=True)
    
    ticker_id = \
        models.ForeignKey(Ticker,
                          on_delete=models.CASCADE,
                          verbose_name='TickerID',
                          db_column='ticker_id',
                          default=0,
                          null=False,
                          blank=False)
    
    close_date = \
        models.DateField(verbose_name='Close Date',
                         db_column='close_date',
                         default=date.today,
                         null=False,
                         blank=False)
    
    #-------------------------------------------------------------------------
    # DATA_SOURCE TYPES
    #-------------------------------------------------------------------------
    DATA_SOURCE_NONE = 0
    DATA_SOURCE_FLAT_FILE = 1
    DATA_SOURCE__TYPES = ( 
        (DATA_SOURCE_NONE,      '<None>'), 
        (DATA_SOURCE_FLAT_FILE, 'File')
    )    
    data_source = \
        models.SmallIntegerField(verbose_name='Data Source',
                                 db_column='data_source',
                                 choices=DATA_SOURCE__TYPES,
                                 default=DATA_SOURCE_NONE,
                                 null=False,
                                 blank=False)
    
    open_value = \
        models.FloatField(verbose_name='Open',
                          db_column='open_value',
                          null=True,
                          blank=True)
    
    high_value = \
        models.FloatField(verbose_name='High',
                          db_column='high_value',
                          null=True,
                          blank=True)

    low_value = \
        models.FloatField(verbose_name='Low',
                          db_column='low_value',
                          null=True,
                          blank=True)
    
    close_value = \
        models.FloatField(verbose_name='Close',
                          db_column='close_value',
                          null=True,
                          blank=True)
    
    volume = \
        models.FloatField(verbose_name='Volume',
                          db_column='volume',
                          null=True,
                          blank=True)

    # NOTE: This will be used in early versions of the system until TickerEodDataAuditRecord is implemented
    created_timestamp = \
        models.DateTimeField(verbose_name='Created',
                             db_column='created_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)
    
    # NOTE: This will be used in early versions of the system until TickerEodDataAuditRecord is implemented
    updated_timestamp = \
        models.DateTimeField(verbose_name='Updated',
                             db_column='updated_timestamp',
                             default=timezone.now,
                             null=True,
                             blank=True)

    class Meta:
        db_table = 'ticker_eod_data'
        unique_together = ('ticker_id', 'close_date')
    
    def __str__(self): 
        return self.name


#-----------------------------------------------------------------------------
# TickerEodDataAuditRecord
#
# NOTE: This will NOT be used in early versions of the system.
#-----------------------------------------------------------------------------
"""
class TickerEodDataAuditRecord(models.Model):

    audit_id = \
        models.BigAutoField(verbose_name='AuditID',
                            db_column='audit_id',
                            primary_key=True)
    
    #-------------------------------------------------------------------------
    # AUDIT_ACTION_TYPES
    #-------------------------------------------------------------------------
    AUDIT_ACTION_INSERT = 1
    AUDIT_ACTION_UPDATE = 0
    AUDIT_ACTION_DELETE = -1
    AUDIT_ACTION__TYPES = ( 
        (AUDIT_ACTION_INSERT, 'Insert'),
        (AUDIT_ACTION_UPDATE, 'Update'),
        (AUDIT_ACTION_DELETE, 'Delete')
    )
    audit_action = \
        models.SmallIntegerField(verbose_name='Audit Action',
                                 db_column='audit_action',
                                 choices=AUDIT_ACTION__TYPES,
                                 default=AUDIT_ACTION_UPDATE,
                                 null=False,
                                 blank=False)
    
    audit_timestamp = \
        models.DateTimeField(verbose_name='Audit Timestamp',
                             db_column='audit_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)
    
    
    ticker_eod_data_id = \
        models.BigIntegerField(verbose_name='TickerEodDataID',
                               db_column='ticker_eod_data_id',
                               default=0,
                               null=False,
                               blank=False)
    
    ticker_id = \
        models.ForeignKey(Ticker,
                          on_delete=models.CASCADE,
                          verbose_name='TickerID',
                          db_column='ticker_id',
                          default=0,
                          null=False,
                          blank=False)
    
    close_date = \
        models.DateField(verbose_name='Close Date',
                         db_column='close_date',
                         default=date.today,
                         null=False,
                         blank=False)
    
    data_source = \
        models.ForeignKey('reference_data.ResourceType',
                          on_delete=models.PROTECT,
                          verbose_name='DataSource',
                          db_column='data_source',
                          default=0,
                          null=False,
                          blank=False)
    
    open_value = \
        models.FloatField(verbose_name='Open',
                          db_column='open_value',
                          null=True,
                          blank=True)
    
    high_value = \
        models.FloatField(verbose_name='High',
                          db_column='high_value',
                          null=True,
                          blank=True)

    low_value = \
        models.FloatField(verbose_name='Low',
                          db_column='low_value',
                          null=True,
                          blank=True)
    
    close_value = \
        models.FloatField(verbose_name='Close',
                          db_column='close_value',
                          null=True,
                          blank=True)
    
    volume = \
        models.FloatField(verbose_name='Volume',
                          db_column='volume',
                          null=True,
                          blank=True)

    class Meta:
        db_table = 'ticker_eod_data_audit_record'

    def __str__(self): 
        return self.name
"""