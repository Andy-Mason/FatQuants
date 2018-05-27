from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


#-----------------------------------------------------------------------------
# Country
#-----------------------------------------------------------------------------
class Country(models.Model):

    country_code = \
        models.CharField(verbose_name='CountryCode',
                         db_column='country_code',
                         max_length=2,
                         primary_key=True)

    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
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

    currency_code = \
        models.CharField(verbose_name='Ccy',
                         db_column='currency_code',
                         max_length=3,
                         primary_key=True)

    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100,
                         unique=True,
                         null=False,
                         blank=False)
    
    base_currency_units = \
        models.FloatField(verbose_name='BaseCcy Units',
                          db_column='base_currency_units',
                          null=True,
                          blank=True)
    
    base_currency_code = \
        models.ForeignKey('self',
                          on_delete=models.PROTECT,
                          verbose_name='BaseCcy',
                          db_column='base_currency_code',
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

    identifier_type = \
        models.CharField(verbose_name='Identifier Type',
                         db_column='identifier_type',
                         max_length=20,
                         primary_key=True)

    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
                         unique=True,
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
        models.AutoField(verbose_name='MarketIndexID',
                         db_column='market_index_id',
                         primary_key=True)

    market_index = \
        models.CharField(verbose_name='Market Index',
                         db_column='market_index',
                         max_length=100,
                         unique=True,
                         default='',
                         null=False,
                         blank=False)

    order_by = \
        models.IntegerField(verbose_name='Order By',
                            db_column='order_by',
                            null=True,
                            blank=True)
    
    notes = \
        models.CharField(verbose_name='Notes',
                         db_column='notes',
                         max_length=250,
                         default='',
                         null=False,
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
        models.IntegerField(verbose_name='ResourceType',
                            db_column='resource_type',
                            primary_key=True)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
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

    test_identifier = \
        models.CharField(verbose_name='Test Identifier',
                         db_column='test_identifier',
                         max_length=63,
                         primary_key=True)

    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
                         unique=True,
                         null=False,
                         blank=False)

    notes = \
        models.CharField(verbose_name='Notes',
                         db_column='notes',
                         max_length=250,
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
    
    test_decimal = \
        models.DecimalField(verbose_name='Decimal',
                            db_column='test_decimal',
                            max_digits=40,
                            decimal_places=20,
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
# TradingExchange
#-----------------------------------------------------------------------------
class TradingExchange(models.Model):

    trading_exchange = \
        models.CharField(verbose_name='Trading Exchange',
                         db_column='trading_exchange',
                         max_length=20,
                         primary_key=True)

    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
                         unique=True,
                         null=False,
                         blank=False)

    class Meta:
        db_table = 'refdata_trading_exchange'

    def __str__(self):
        return self.name
