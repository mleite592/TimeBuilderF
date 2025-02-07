from peewee import Model, CharField, IntegerField, DateField, DateTimeField
from database.database import BaseModel

class Timesheet(BaseModel):
    operator = CharField(null=True)
    timesheet_date = DateField(null=True)
    projectId = IntegerField(null=True)    
    unit_name = CharField(null=True)
    sub_unit_name = CharField(null=True)
    sub_taskId = CharField(null=True)
    start_chainage = IntegerField(null=True)
    end_chainage = IntegerField(null=True)
    task_status = CharField(null=True)
    type_feature = CharField(null=True)  # Traditional or Roames
    type_task = CharField(null=True)     # Rework or QC
    comments = CharField(null=True)    
    start_time = DateTimeField(null=True)
    end_time = DateTimeField(null=True)       
    status = CharField(null=True)  # Open, Submitted, Approved, Deleted