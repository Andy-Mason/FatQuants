from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


#-----------------------------------------------------------------------------
# Country
#-----------------------------------------------------------------------------
class Country(models.Model):

    country_id = \
        models.BigAutoField(verbose_name='CountryID',
                            db_column='country_id',
                            primary_key=True)

    country_code = \
        models.CharField(verbose_name='CountryCode',
                         db_column='country_code',
                         max_length=2,
                         unique=True,
                         null=False,
                         blank=False)

    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250, 
                         unique=True,
                         null=False,
                         blank=False)

    class Meta:
        db_table = 'refdata_country'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# Currency
#-----------------------------------------------------------------------------
class Currency(models.Model):

    currency_id = \
        models.BigAutoField(verbose_name='CurrencyID',
                            db_column='currency_id',
                            primary_key=True)

    currency_code = \
        models.CharField(verbose_name='Ccy',
                         db_column='currency_code',
                         max_length=3,
                         unique=True,
                         null=False,
                         blank=False)

    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250,
                         unique=True,
                         null=False,
                         blank=False)
    
    base_currency_code = \
        models.ForeignKey('self',
                          to_field='currency_code',
                          on_delete=models.PROTECT,
                          verbose_name='BaseCcy',
                          db_column='base_currency_code',
                          null=True,
                          blank=True)
    
    base_currency_units = \
        models.FloatField(verbose_name='BaseCcy Units',
                          db_column='base_currency_units',
                          null=True,
                          blank=True)    
    
    class Meta:
        db_table = 'refdata_currency'

    def __str__(self): 
        return self.name


#-----------------------------------------------------------------------------
# IdentifierType
#-----------------------------------------------------------------------------
class IdentifierType(models.Model):

    identifier_type_id = \
        models.BigAutoField(verbose_name='IdentifierTypeID',
                            db_column='identifier_type_id',
                            primary_key=True)

    identifier_type = \
        models.CharField(verbose_name='IdentifierType',
                         db_column='identifier_type',
                         max_length=30,
                         unique=True,
                         null=False,
                         blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250, 
                         unique=True,
                         default='',
                         null=False,
                         blank=False)
    
    class Meta:
        db_table = 'refdata_identifier_type'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# MarketIndex
#-----------------------------------------------------------------------------
class MarketIndex(models.Model):

    market_index_id = \
        models.BigAutoField(verbose_name='MarketIndexID',
                            db_column='market_index_id',
                            primary_key=True)

    market_index = \
        models.CharField(verbose_name='MarketIndex',
                         db_column='market_index',
                         max_length=100,
                         unique=True,
                         default='',
                         null=False,
                         blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250,
                         default='',
                         null=False,
                         blank=True)
    
    order_by = \
        models.BigIntegerField(verbose_name='Order By',
                               db_column='order_by',
                               null=True,
                               blank=True)
    
    class Meta:
        db_table = 'refdata_market_index'

    def __str__(self): 
        return self.name


#-----------------------------------------------------------------------------
# ResourceType
#-----------------------------------------------------------------------------
class ResourceType(models.Model):

    resource_type = \
        models.BigIntegerField(verbose_name='ResourceType',
                               db_column='resource_type',
                               primary_key=True)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250, 
                         unique=True,
                         default='',
                         null=False,
                         blank=False)

    class Meta:
        db_table = 'refdata_resource_type'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# TestData
#-----------------------------------------------------------------------------
class TestData(models.Model):

    test_identifier_id = \
        models.BigAutoField(verbose_name='TestIdentifierID',
                            db_column='test_identifier_id',
                            primary_key=True)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250, 
                         unique=True,
                         default='',
                         null=False,
                         blank=False)

    notes = \
        models.CharField(verbose_name='Notes',
                         db_column='notes',
                         max_length=1000,
                         null=True,
                         blank=True)
    
    test_boolean = \
        models.NullBooleanField(verbose_name='Boolean',
                                db_column='test_boolean',
                                null=True,
                                blank=True)
    
    test_smallint = \
        models.SmallIntegerField(verbose_name='Small Integer',
                                 db_column='test_smallint',
                                 null=True,
                                 blank=True)    
    
    test_integer = \
        models.IntegerField(verbose_name='Integer',
                               db_column='test_integer',
                               null=True,
                               blank=True)
    
    test_bigint = \
        models.BigIntegerField(verbose_name='Big Integer',
                               db_column='test_bigint',
                               null=True,
                               blank=True)
    
    test_float = \
        models.FloatField(verbose_name='Float',
                          db_column='test_float',
                          null=True,
                          blank=True)
    
    #-------------------------------------------------------------------------
    # Decimal (Numeric) data type
    #-------------------------------------------------------------------------
    # Django limits : max_digits=1000, decimal_places=500
    # ODBC limits   : max_digits=254,  decimal_places=127
    #-------------------------------------------------------------------------
    test_decimal = \
        models.DecimalField(verbose_name='Decimal',
                            db_column='test_decimal',
                            max_digits=254,
                            decimal_places=127,
                            null=True,
                            blank=True)
    
    test_date = \
        models.DateField(verbose_name='Date',
                         db_column='test_date',
                         null=True,
                         blank=True)
    
    test_time = \
        models.TimeField(verbose_name='Time',
                         db_column='test_time',
                         null=True,
                         blank=True)
    
    test_datetime = \
        models.DateTimeField(verbose_name='DateTime',
                             db_column='test_datetime',
                             null=True,
                             blank=True)
    
    test_duration = \
        models.DurationField(verbose_name='Duration',
                             db_column='test_duration',
                             null=True,
                             blank=True)
    
    test_text = \
        models.TextField(verbose_name='Text',
                         db_column='test_text',
                         null=True,
                         blank=True)
    
    test_inet = \
        models.GenericIPAddressField(verbose_name='Generic IP Address',
                                     db_column='test_inet',
                                     null=True,
                                     blank=True)
    
    test_uuid = \
        models.UUIDField(verbose_name='UUID',
                         db_column='test_uuid',
                         null=True,
                         blank=True)
    
    test_json = \
        JSONField(verbose_name='JSON',
                  db_column='test_json',
                  null=True,
                  blank=True)
    
    test_blob = \
        models.BinaryField(verbose_name='BLOB',
                           db_column='test_blob',
                           null=True,
                           blank=True)
    
    class Meta:
        db_table = 'refdata_test'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# TextTranslation
#-----------------------------------------------------------------------------
class TextTranslation(models.Model):

    text_translation_id = \
        models.BigAutoField(verbose_name='TextTranslationID',
                            db_column='text_translation_id',
                            primary_key=True)

    text_context = \
        models.CharField(verbose_name='TextContext',
                         db_column='text_context',
                         max_length=100,
                         null=False,
                         blank=False)
    
    text_lookup = \
        models.TextField(verbose_name='TextLookup',
                         db_column='text_lookup',
                         null=False,
                         blank=False)
    
    text_translation = \
        models.TextField(verbose_name='TextTranslation',
                         db_column='text_translation',
                         null=False,
                         blank=True)
    
    class Meta:
        db_table = 'refdata_text_translation'
        unique_together = ('text_context', 'text_lookup')

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# TradingExchange
#-----------------------------------------------------------------------------
class TradingExchange(models.Model):

    trading_exchange_id = \
        models.BigAutoField(verbose_name='TradingExchangeID',
                            db_column='trading_exchange_id',
                            primary_key=True)

    trading_exchange = \
        models.CharField(verbose_name='TradingExchange',
                         db_column='trading_exchange',
                         max_length=30,
                         unique=True,
                         null=False,
                         blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250, 
                         unique=True,
                         default='',
                         null=False,
                         blank=False)
    
    class Meta:
        db_table = 'refdata_trading_exchange'

    def __str__(self):
        return self.name
