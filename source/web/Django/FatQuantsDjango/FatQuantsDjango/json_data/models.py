from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


#-----------------------------------------------------------------------------
# JsonData
#-----------------------------------------------------------------------------
class JsonData(models.Model):

    json_data_id = \
        models.BigAutoField(verbose_name='JsonDataID',
                            db_column='json_data_id',
                            primary_key=True)

    base_json_data_id = \
        models.ForeignKey('self',
                          on_delete=models.CASCADE,
                          verbose_name='BaseJsonDataID',
                          db_column='base_json_data_id',
                          null=True,
                          blank=True)

    #-------------------------------------------------------------------------
    # ERROR CODES
    #-------------------------------------------------------------------------
    ERROR_NONE           = 0
    ERROR_DATA_SOURCE    = 1
    ERROR_JSON_PARSER    = 2
    ERROR_DATA_INTEGRITY = 3
    ERROR__CODES = ( 
        (ERROR_NONE,            '<None>'), 
        (ERROR_DATA_SOURCE,     'Data Source Error'), 
        (ERROR_JSON_PARSER,     'JSON Parser Error'),
        (ERROR_DATA_INTEGRITY,  'Data Integrity Error')
    )
    error_code = \
       models.SmallIntegerField(verbose_name='ErrorCode',
                                db_column='error_code',
                                choices=ERROR__CODES,
                                default=ERROR_NONE,
                                null=False,
                                blank=False)
    
    data_tag = \
        models.CharField(verbose_name='DataTag',
                         db_column='data_tag',
                         max_length=100,
                         default='',
                         null=False,
                         blank=True)
    
    identifier = \
        models.TextField(verbose_name='Identifier',
                         db_column='identifier',
                         default='',
                         null=False,
                         blank=True)
    
    description = \
        models.TextField(verbose_name='Description',
                         db_column='description',
                         default='',
                         null=False,
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
        db_table = 'json_data'

    def __str__(self):
        return self.name
