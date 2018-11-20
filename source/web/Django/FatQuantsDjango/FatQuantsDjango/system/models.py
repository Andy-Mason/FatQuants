from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


#-----------------------------------------------------------------------------
# SystemAuditRecord
#-----------------------------------------------------------------------------
class SystemAuditRecord(models.Model):

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
    
    table_name = \
        models.CharField(verbose_name='Table Name',
                         db_column='table_name',
                         max_length=63,
                         default='',
                         null=False,
                         blank=False)
    
    primary_key_field_name = \
        models.CharField(verbose_name='Primary Key Field',
                         db_column='primary_key_field_name',
                         max_length=63,
                         default='',
                         null=False,
                         blank=False)
    
    primary_key_field_value = \
        models.BigIntegerField(verbose_name='Primary Key Value',
                               db_column='primary_key_field_value',
                               default=0,
                               null=False,
                               blank=False)
    
    field_name = \
        models.CharField(verbose_name='Field Name',
                         db_column='field_name',
                         max_length=63,
                         default='',
                         null=False,
                         blank=False)
    
    field_data_type = \
        models.ForeignKey('SystemDataType',
                          on_delete=models.PROTECT,
                          verbose_name='Field DataType',
                          db_column='field_data_type',
                          default=0,
                          null=False,
                          blank=False)
    
    field_value_boolean = \
        models.NullBooleanField(verbose_name='Boolean',
                                db_column='field_value_boolean',
                                null=True,
                                blank=True)
    
    field_value_integer = \
        models.BigIntegerField(verbose_name='Integer',
                               db_column='field_value_integer',
                               null=True,
                               blank=True)
    
    field_value_float = \
        models.FloatField(verbose_name='Float',
                          db_column='field_value_float',
                          null=True,
                          blank=True)
    
    field_value_decimal = \
        models.DecimalField(verbose_name='Decimal',
                            db_column='field_value_decimal',
                            max_digits=1000,
                            decimal_places=500,
                            null=True,
                            blank=True)
    
    field_value_date = \
        models.DateField(verbose_name='Date',
                         db_column='field_value_date',
                         null=True,
                         blank=True)
    
    field_value_time = \
        models.TimeField(verbose_name='Time',
                         db_column='field_value_time',
                         null=True,
                         blank=True)
    
    field_value_datetime = \
        models.DateTimeField(verbose_name='DateTime',
                             db_column='field_value_datetime',
                             null=True,
                             blank=True)
    
    field_value_duration = \
        models.DurationField(verbose_name='Duration',
                             db_column='field_value_duration',
                             null=True,
                             blank=True)
    
    field_value_text = \
        models.TextField(verbose_name='Text',
                         db_column='field_value_text',
                         null=True,
                         blank=True)
    
    field_value_json = \
        JSONField(verbose_name='JSON',
                  db_column='field_value_json',
                  null=True,
                  blank=True)
    
    field_value_blob = \
        models.BinaryField(verbose_name='BLOB',
                           db_column='field_value_blob',
                           null=True,
                           blank=True)
    
    class Meta:
        db_table = 'system_audit_record'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# SystemDataType
#-----------------------------------------------------------------------------
class SystemDataType(models.Model):

    system_data_type = \
        models.SmallIntegerField(verbose_name='SystemDataType',
                                 db_column='system_data_type',
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
                         default='',
                         null=False,
                         blank=True)

    class Meta:
        db_table = 'system_data_type'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# SystemDataTypeMapping
#-----------------------------------------------------------------------------
class SystemDataTypeMapping(models.Model):

    database_data_type = \
        models.CharField(verbose_name='Database DataType',
                         db_column='database_data_type',
                         max_length=63,
                         primary_key=True)

    system_data_type = \
        models.ForeignKey('system.SystemDataType',
                          on_delete=models.PROTECT,
                          verbose_name='SystemDataType',
                          db_column='system_data_type',
                          default=0,
                          null=False,
                          blank=False)

    class Meta:
        db_table = 'system_data_type_mapping'

    def __str__(self):
        return self.name
