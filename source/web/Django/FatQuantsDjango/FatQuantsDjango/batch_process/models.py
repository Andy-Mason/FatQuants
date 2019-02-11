from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


#-----------------------------------------------------------------------------
# BatchProcessType
#-----------------------------------------------------------------------------
class BatchProcessType(models.Model):

    batch_process_type_id = \
        models.AutoField(verbose_name='BatchProcessTypeID',
                         db_column='batch_process_type_id',
                         primary_key=True)
    
    batch_process_type_tag = \
        models.CharField(verbose_name='BatchProcessTypeTag',
                         db_column='batch_process_type_tag',
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
                         default='',
                         null=False,
                         blank=True)
    
    execution_handler = \
        models.CharField(verbose_name='ExecutionHandler',
                         db_column='execution_handler',
                         max_length=100,
                         default='',
                         null=False,
                         blank=False)
    
    configuration = \
        JSONField(verbose_name='Configuration',
                  db_column='configuration',
                  null=True,
                  blank=True)
    
    class Meta:
        db_table = 'batch_process_type'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# BatchProcess
#-----------------------------------------------------------------------------
class BatchProcess(models.Model):

    batch_process_id = \
        models.BigAutoField(verbose_name='BatchProcessID',
                            db_column='batch_process_id',
                            primary_key=True)
    
    
    batch_process_type_id = \
        models.ForeignKey(BatchProcessType,
                          on_delete=models.PROTECT,
                          verbose_name='BatchProcessTypeID',
                          db_column='batch_process_type_id',
                          default=0,
                          null=False,
                          blank=False)
    
    batch_process_tag = \
        models.CharField(verbose_name='BatchProcessTag',
                         db_column='batch_process_tag',
                         max_length=50, 
                         default='',
                         null=False,
                         blank=True)
    
    test_instance = \
        models.BooleanField(verbose_name='TestInstance',
                            db_column='test_instance',
                            default=False,
                            null=False,
                            blank=False)

    #-------------------------------------------------------------------------
    # PROCESS_STATUS TYPES
    #-------------------------------------------------------------------------
    PROCESS_STATUS_PENDING = 0
    PROCESS_STATUS_RUNNING = 1
    PROCESS_STATUS_FINISHED = 2
    PROCESS_STATUS_ABORTED = -1
    PROCESS_STATUS_CANCELLING = -2
    PROCESS_STATUS_CANCELLED = -3
    PROCESS_STATUS__TYPES = ( 
        (PROCESS_STATUS_PENDING,    'Pending'), 
        (PROCESS_STATUS_RUNNING,    'Running...'), 
        (PROCESS_STATUS_FINISHED,   'Finished'),
        (PROCESS_STATUS_ABORTED,    'Aborted'),
        (PROCESS_STATUS_CANCELLING, 'Cancelling...'),
        (PROCESS_STATUS_CANCELLED,  'Cancelled')
    )
    process_status = \
       models.SmallIntegerField(verbose_name='ProcessStatus',
                                db_column='process_status',
                                choices=PROCESS_STATUS__TYPES,
                                default=PROCESS_STATUS_PENDING,
                                null=False,
                                blank=False)
    
    json_data_id = \
        models.ForeignKey('json_data.JsonData',
                          on_delete=models.PROTECT,
                          verbose_name='JsonDataID',
                          db_column='json_data_id',
                          default=0,
                          null=False,
                          blank=False)
    
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
        db_table = 'batch_process'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# BatchProcessLog
#-----------------------------------------------------------------------------
class BatchProcessLog(models.Model):

    batch_process_log_id = \
        models.BigAutoField(verbose_name='BatchProcessLogID',
                            db_column='batch_process_log_id',
                            primary_key=True)
    
    batch_process_id = \
        models.ForeignKey(BatchProcess,
                          on_delete=models.CASCADE,
                          verbose_name='BatchProcessID',
                          db_column='batch_process_id',
                          default=0,
                          null=False,
                          blank=False)

    #-------------------------------------------------------------------------
    # PROCESS_ACTION TYPES
    #-------------------------------------------------------------------------
    PROCESS_ACTION_CANCEL       = -1
    PROCESS_ACTION_NONE         = 0
    PROCESS_ACTION_RUN          = 1
    PROCESS_ACTION_RESUME       = 2
    PROCESS_ACTION_RERUN_ERRORS = 3
    PROCESS_ACTION_RERUN_ALL    = 4
    PROCESS_ACTION__TYPES = ( 
        (PROCESS_ACTION_CANCEL,       'Cancel'), 
        (PROCESS_ACTION_NONE,         '<None>'), 
        (PROCESS_ACTION_RUN,          'Run'), 
        (PROCESS_ACTION_RESUME,       'Resume'), 
        (PROCESS_ACTION_RERUN_ERRORS, 'ReRun Errors'), 
        (PROCESS_ACTION_RERUN_ALL,    'ReRun All')
    )
    process_action = \
       models.SmallIntegerField(verbose_name='ProcessAction',
                                db_column='process_action',
                                choices=PROCESS_ACTION__TYPES,
                                null=True,
                                blank=True)
    
    log_timestamp = \
        models.DateTimeField(verbose_name='TimeStamp',
                             db_column='log_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)
    
    #-------------------------------------------------------------------------
    # LOG_ENTRY TYPES
    #-------------------------------------------------------------------------
    LOG_ENTRY_DEBUG = 'DEBUG'
    LOG_ENTRY_TRACE = 'TRACE'
    LOG_ENTRY_INFO  = 'INFO'
    LOG_ENTRY_WARN  = 'WARN'
    LOG_ENTRY_ERROR = 'ERROR'
    LOG_ENTRY_FATAL = 'FATAL'
    LOG_ENTRY__TYPES = ( 
        (LOG_ENTRY_DEBUG, 'Debug'), 
        (LOG_ENTRY_TRACE, 'Trace'), 
        (LOG_ENTRY_INFO,  'Informational'), 
        (LOG_ENTRY_WARN,  'Warning'), 
        (LOG_ENTRY_ERROR, 'Error'), 
        (LOG_ENTRY_FATAL, 'Fatal')
    )
    log_entry_type = \
        models.CharField(verbose_name='Type',
                         db_column='log_entry_type',
                         max_length=5, 
                         choices=LOG_ENTRY__TYPES,
                         default=LOG_ENTRY_INFO,
                         null=False,
                         blank=False)
    
    log_message = \
        models.TextField(verbose_name='Log Message',
                         db_column='log_message',
                         default='',
                         null=False,
                         blank=False)
    
    class Meta:
        db_table = 'batch_process_log'

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# BatchProcessTask
#-----------------------------------------------------------------------------
class BatchProcessTask(models.Model):

    batch_process_task_id = \
        models.BigAutoField(verbose_name='BatchProcessTaskID',
                            db_column='batch_process_task_id',
                            primary_key=True)
    
    batch_process_id = \
        models.ForeignKey(BatchProcess,
                          on_delete=models.CASCADE,
                          verbose_name='BatchProcessID',
                          db_column='batch_process_id',
                          default=0,
                          null=False,
                          blank=False)
    
    task_number = \
        models.PositiveIntegerField(verbose_name='TaskNumber',
                                    db_column='task_number',
                                    default=0,
                                    null=False,
                                    blank=False)
    
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
        db_table = 'batch_process_task'
        unique_together = ('batch_process_id', 'task_number')

    def __str__(self):
        return self.name


#-----------------------------------------------------------------------------
# BatchProcessTaskIntervention
#-----------------------------------------------------------------------------
class BatchProcessTaskIntervention(models.Model):

    id = \
        models.BigAutoField(verbose_name='ID',
                            db_column='id',
                            primary_key=True)
    
    batch_process_task_id = \
        models.ForeignKey(BatchProcessTask,
                          on_delete=models.CASCADE,
                          verbose_name='BatchProcessTaskID',
                          db_column='batch_process_task_id',
                          default=0,
                          null=False,
                          blank=False)
    
    intervention_timestamp = \
        models.DateTimeField(verbose_name='TimeStamp',
                             db_column='intervention_timestamp',
                             default=timezone.now,
                             null=False,
                             blank=False)
    
    #-------------------------------------------------------------------------
    # INTERVENTION TYPES
    #-------------------------------------------------------------------------
    INTERVENTION_CANCELLED = -1
    INTERVENTION_NONE      = 0
    INTERVENTION_RESUMED   = 1
    INTERVENTION__TYPES = ( 
        (INTERVENTION_CANCELLED, 'Cancelled'), 
        (INTERVENTION_NONE,      '<None>'), 
        (INTERVENTION_RESUMED,   'Resumed')
    )
    intervention_type = \
       models.SmallIntegerField(verbose_name='InterventionType',
                                db_column='intervention_type',
                                choices=INTERVENTION__TYPES,
                                default=INTERVENTION_NONE,
                                null=False,
                                blank=False)
    
    class Meta:
        db_table = 'batch_process_task_intervention'

    def __str__(self):
        return self.name

