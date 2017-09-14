from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


#-----------------------------------------------------------------------------
# ProcessType
#-----------------------------------------------------------------------------
class ProcessType(models.Model):

    process_type_id = \
        models.AutoField(verbose_name='ProcessTypeID',
                         db_column='process_type_id',
                         primary_key=True)

    base_process_type_id = \
        models.ForeignKey('self',
                          on_delete=models.CASCADE,
                          verbose_name='BaseProcessTypeID',
                          db_column='base_process_type_id',
                          null=True,
                          blank=True)
    
    sequence_number = \
        models.IntegerField(verbose_name='SequenceNumber',
                            db_column='sequence_number',
                            default=0,
                            null=False,
                            blank=False)
    
    process_type_tag = \
        models.CharField(verbose_name='ProcessTypeTag',
                         db_column='process_type_tag',
                         max_length=50, 
                         default='',
                         null=False,
                         blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
                         default='',
                         null=False,
                         blank=False)

    notes = \
        models.CharField(verbose_name='Notes',
                         db_column='notes',
                         max_length=250, 
                         null=True,
                         blank=True)

    execution_handler = \
        models.CharField(verbose_name='ExecutionHandler',
                         db_column='execution_handler',
                         max_length=100, 
                         null=True,
                         blank=True)
    
    configuration = \
        JSONField(verbose_name='Configuration',
                  db_column='configuration',
                  null=True,
                  blank=True)

    run_item_units = \
        models.CharField(verbose_name='RunItemUnits',
                         db_column='run_item_units',
                         max_length=50, 
                         null=True,
                         blank=True)

    class Meta:
        db_table = 'process_type'
        unique_together = (
            ('base_process_type_id', 'sequence_number'),
            ('base_process_type_id', 'process_type_tag'),
            ('base_process_type_id', 'description')
        )

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# ProcessTypeJSONDataSetType
#-----------------------------------------------------------------------------
class ProcessTypeJSONDataSetType(models.Model):

    id = \
        models.AutoField(verbose_name='ID',
                         db_column='id',
                         primary_key=True,
                         unique=True)

    process_type_id = \
        models.ForeignKey(ProcessType,
                          on_delete=models.CASCADE,
                          verbose_name='ProcessTypeID',
                          db_column='process_type_id',
                          default=0,
                          null=False,
                          blank=False)
    
    data_set_type_id = \
        models.ForeignKey('json_data.JSONDataSetType',
                          on_delete=models.CASCADE,
                          verbose_name='DataSetTypeID',
                          db_column='data_set_type_id',
                          default=0,
                          null=False,
                          blank=False)

    class Meta:
        db_table = 'process_type_json_data_set_type'
        unique_together = ('process_type_id', 'data_set_type_id')

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# Process
#-----------------------------------------------------------------------------
class Process(models.Model):

    process_id = \
        models.BigAutoField(verbose_name='ProcessID',
                            db_column='process_id',
                            primary_key=True)

    base_process_id = \
        models.ForeignKey('self',
                          on_delete=models.CASCADE,
                          verbose_name='BaseProcessID',
                          db_column='base_process_id',
                          null=True,
                          blank=True)
    
    process_type_id = \
        models.ForeignKey(ProcessType,
                          on_delete=models.PROTECT,
                          verbose_name='ProcessTypeID',
                          db_column='process_type_id',
                          default=0,
                          null=False,
                          blank=False)
    
    description = \
        models.CharField(verbose_name='Description',
                         db_column='description',
                         max_length=100, 
                         default='',
                         null=False,
                         blank=False)

    #-------------------------------------------------------------------------
    # RUN_TYPES
    #-------------------------------------------------------------------------
    RUN_TEST         = -1
    RUN_NORMAL       = 0
    RUN_RERUN_ALL    = 1
    RUN_RERUN_RESUME = 2
    RUN_RERUN_ERRORS = 3
    RUN__TYPES = ( 
        (RUN_TEST,         'Test Run'), 
        (RUN_NORMAL,       'Normal Run'), 
        (RUN_RERUN_ALL,    'ReRun All'), 
        (RUN_RERUN_RESUME, 'ReRun Resume'), 
        (RUN_RERUN_ERRORS, 'ReRun Errors') 
    )
    run_type = \
        models.SmallIntegerField(verbose_name='RunType',
                                 db_column='run_type',
                                 choices=RUN__TYPES,
                                 default=0,
                                 null=False,
                                 blank=False)

    #-------------------------------------------------------------------------
    # RUNSTATUS_TYPES
    #-------------------------------------------------------------------------    
    RUNSTATUS_PENDING = -1
    RUNSTATUS_RUNNING = 0
    RUNSTATUS_FINISHED = 1
    RUNSTATUS__TYPES = ( 
        (RUNSTATUS_PENDING,  'Pending'), 
        (RUNSTATUS_RUNNING,  'Running...'), 
        (RUNSTATUS_FINISHED, 'Finished') 
    )
    run_status = \
       models.SmallIntegerField(verbose_name='RunStatus',
                                 db_column='run_status',
                                 choices=RUNSTATUS__TYPES,
                                 default=RUNSTATUS_PENDING,
                                 null=False,
                                 blank=False)
    
    run_status_message = \
        models.CharField(verbose_name='StatusMessage',
                         db_column='run_status_message',
                         max_length=100, 
                         default='',
                         null=True,
                         blank=True)
    
    run_start_time = \
        models.DateTimeField(verbose_name='StartTime',
                             db_column='run_start_time',
                             null=True,
                             blank=True)
    
    run_finish_time = \
        models.DateTimeField(verbose_name='FinishTime',
                             db_column='run_finish_time',
                             null=True,
                             blank=True)
    
    run_done_items = \
        models.PositiveIntegerField(verbose_name='Done',
                                    db_column='run_done_items',
                                    null=True,
                                    blank=True)

    run_error_items = \
        models.PositiveIntegerField(verbose_name='Errors',
                                    db_column='run_error_items',
                                    null=True,
                                    blank=True)

    run_total_items = \
        models.PositiveIntegerField(verbose_name='Total',
                                    db_column='run_total_items',
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
        db_table = 'process'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# ProcessJSONDataSet
#-----------------------------------------------------------------------------
class ProcessJSONDataSet(models.Model):

    id = \
        models.BigAutoField(verbose_name='ID',
                            db_column='id',
                            primary_key=True)

    process_id = \
        models.ForeignKey(Process,
                          on_delete=models.CASCADE,
                          verbose_name='ProcessID',
                          db_column='process_id',
                          default=0,
                          null=False,
                          blank=False)
    
    data_set_id = \
        models.ForeignKey('json_data.JSONDataSet',
                          on_delete=models.CASCADE,
                          verbose_name='DataSetID',
                          db_column='data_set_id',
                          default=0,
                          null=False,
                          blank=False)
    
    created_timestamp = \
        models.DateTimeField(verbose_name='Created',
                             db_column='created_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)

    class Meta:
        db_table = 'process_json_data_set'
        unique_together = ('process_id', 'data_set_id')

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# ProcessLog
#-----------------------------------------------------------------------------
class ProcessLog(models.Model):

    process_log_id = \
        models.BigAutoField(verbose_name='ProcessLogID',
                            db_column='process_log_id',
                            primary_key=True)
    
    process_id = \
        models.ForeignKey(Process,
                          on_delete=models.CASCADE,
                          verbose_name='ProcessID',
                          db_column='process_id',
                          default=0,
                          null=False,
                          blank=False)
    
    log_timestamp = \
        models.DateTimeField(verbose_name='TimeStamp',
                             db_column='log_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)

    #-------------------------------------------------------------------------
    # LOGENTRY_TYPES
    #-------------------------------------------------------------------------
    LOGENTRY_DEBUG = 'DEBUG'
    LOGENTRY_TRACE = 'TRACE'
    LOGENTRY_INFO  = 'INFO'
    LOGENTRY_WARN  = 'WARN'
    LOGENTRY_ERROR = 'ERROR'
    LOGENTRY_FATAL = 'FATAL'
    LOGENTRY__TYPES = ( 
        (LOGENTRY_DEBUG, 'Debug'), 
        (LOGENTRY_TRACE, 'Trace'), 
        (LOGENTRY_INFO,  'Informational'), 
        (LOGENTRY_WARN,  'Warning'), 
        (LOGENTRY_ERROR, 'Error'), 
        (LOGENTRY_FATAL, 'Fatal')
    )
    log_entry_type = \
        models.CharField(verbose_name='Type',
                         db_column='log_entry_type',
                         max_length=5, 
                         choices=LOGENTRY__TYPES,
                         default=LOGENTRY_INFO,
                         null=False,
                         blank=False)

    log_message = \
        models.TextField(verbose_name='Log Message',
                         db_column='log_message',
                         default='',
                         null=False,
                         blank=False)

    class Meta:
        db_table = 'process_log'

    def __str__(self):
        return self.name
