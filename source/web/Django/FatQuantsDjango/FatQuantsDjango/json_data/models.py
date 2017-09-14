from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


#-----------------------------------------------------------------------------
# JSONDataSetType
#-----------------------------------------------------------------------------
class JSONDataSetType(models.Model):

    data_set_type_id = \
        models.AutoField(verbose_name='DataSetTypeID',
                         db_column='data_set_type_id',
                         primary_key=True)

    data_set_type_tag = \
        models.CharField(verbose_name='DataSetTypeTag',
                         db_column='data_set_type_tag',
                         max_length=50,
                         unique=True,
                         default='',
                         null=False,
                         blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
                         unique=True,
                         default='',
                         null=False,
                         blank=False)

    notes = \
        models.CharField(verbose_name='Notes',
                         db_column='notes',
                         max_length=250, 
                         null=True,
                         blank=True)

    class Meta:
        db_table = 'json_data_set_type'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# JSONDataSet
#-----------------------------------------------------------------------------
class JSONDataSet(models.Model):

    data_set_id = \
        models.BigAutoField(verbose_name='DataSetID',
                            db_column='data_set_id',
                            primary_key=True)

    data_set_type_id = \
        models.ForeignKey(JSONDataSetType,
                          on_delete=models.PROTECT,
                          verbose_name='DataSetTypeID',
                          db_column='data_set_type_id',
                          default=0,
                          null=False,
                          blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
                         default='',
                         null=True,
                         blank=True)
    
    created_timestamp = \
        models.DateTimeField(verbose_name='Created',
                             db_column='created_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)
    
    updated_timestamp = \
        models.DateTimeField(verbose_name='Updated',
                             db_column='updated_timestamp',
                             default=timezone.now,
                             null=True,
                             blank=True)

    class Meta:
        db_table = 'json_data_set'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# JSONDataItem
#-----------------------------------------------------------------------------
class JSONDataItem(models.Model):

    data_item_id = \
        models.BigAutoField(verbose_name='DataItemID',
                            db_column='data_item_id',
                            primary_key=True)

    data_set_id = \
        models.ForeignKey(JSONDataSet,
                          on_delete=models.CASCADE,
                          verbose_name='DataSetID',
                          db_column='data_set_id',
                          default=0,
                          null=False,
                          blank=False)

    #-------------------------------------------------------------------------
    # ERROR_CODES
    #-------------------------------------------------------------------------
    ERROR_NONE           = 0
    ERROR_DATA_SOURCE    = 1
    ERROR_JSON_PARSER    = 2
    ERROR_DATA_INTEGRITY = 3
    ERROR_DUPLICATE_ITEM = 4
    ERROR__CODES = ( 
        (ERROR_NONE,            '<None>'), 
        (ERROR_DATA_SOURCE,     'Data Source Error'), 
        (ERROR_JSON_PARSER,     'JSON Parser Error'),
        (ERROR_DATA_INTEGRITY,  'Data Integrity Error'), 
        (ERROR_DUPLICATE_ITEM,  'Duplicate Item Identifier') 
    )
    error_code = \
       models.SmallIntegerField(verbose_name='Error Code',
                                 db_column='error_code',
                                 choices=ERROR__CODES,
                                 default=ERROR_NONE,
                                 null=False,
                                 blank=False)
    
    item_identifier = \
        models.TextField(verbose_name='Item Identifier',
                         db_column='item_identifier',
                         null=True,
                         blank=True)
    
    resource_identifier = \
        models.TextField(verbose_name='Resource Identifier',
                         db_column='resource_identifier',
                         null=True,
                         blank=True)
    
    json_data = \
        JSONField(verbose_name='JSON Data',
                  db_column='json_data',
                  null=True,
                  blank=True)
    
    created_timestamp = \
        models.DateTimeField(verbose_name='Created',
                             db_column='created_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)
    
    updated_timestamp = \
        models.DateTimeField(verbose_name='Updated',
                             db_column='updated_timestamp',
                             default=timezone.now,
                             null=True,
                             blank=True)

    class Meta:
        db_table = 'json_data_item'

    def __str__(self):
        return self.name
