from django.db import models
from django.db.models import JSONField
from django.utils import timezone


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
    
    #-------------------------------------------------------------------------
    # FIELD_DATA_TYPES
    #-------------------------------------------------------------------------
    DATATYPE_NONE     = 0
    DATATYPE_BOOLEAN  = 1
    DATATYPE_INTEGER  = 2
    DATATYPE_FLOAT    = 3
    DATATYPE_DECIMAL  = 4
    DATATYPE_DATE     = 5
    DATATYPE_TIME     = 6
    DATATYPE_DATETIME = 7
    DATATYPE_DURATION = 8
    DATATYPE_TEXT     = 9
    DATATYPE_JSON     = 10
    DATATYPE_BLOB     = 11
    FIELD_DATA_TYPES = (
        (DATATYPE_NONE,     'None'),
        (DATATYPE_BOOLEAN,  'Boolean'),
        (DATATYPE_INTEGER,  'Integer'),
        (DATATYPE_FLOAT,    'Float'),
        (DATATYPE_DECIMAL,  'Decimal'),
        (DATATYPE_DATE,     'Date'),
        (DATATYPE_TIME,     'Time'),
        (DATATYPE_DATETIME, 'DateTime'),
        (DATATYPE_DURATION, 'Duration'),
        (DATATYPE_TEXT,     'Text'),
        (DATATYPE_JSON,     'JSON'),
        (DATATYPE_BLOB,     'BLOB')
    )
    field_data_type = \
        models.SmallIntegerField(verbose_name='Field DataType',
                                 db_column='field_data_type',
                                 choices=FIELD_DATA_TYPES,
                                 default=DATATYPE_NONE,
                                 null=False,
                                 blank=False)
    
    field_value_boolean = \
        models.BooleanField(verbose_name='Boolean',
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
    
    #-------------------------------------------------------------------------
    # Decimal (Numeric) data type
    #-------------------------------------------------------------------------
    # Django limits : max_digits=1000, decimal_places=500
    # ODBC limits   : max_digits=254,  decimal_places=127
    #-------------------------------------------------------------------------
    field_value_decimal = \
        models.DecimalField(verbose_name='Decimal',
                            db_column='field_value_decimal',
                            max_digits=254,
                            decimal_places=127,
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
