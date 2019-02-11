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

    data_tag = \
        models.CharField(verbose_name='DataTag',
                         db_column='data_tag',
                         max_length=50,
                         default='',
                         null=False,
                         blank=True)
    
    identifier = \
        models.CharField(verbose_name='Identifier',
                         db_column='identifier',
                         max_length=100,
                         default='',
                         null=False,
                         blank=True)
    
    ### TODO: DO WE REALLY NEED THIS?
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=250,
                         default='',
                         null=False,
                         blank=True)
    
    resource = \
        models.URLField(verbose_name='Resource',
                        db_column='resource',
                        max_length=2000,
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
