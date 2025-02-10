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

    def calculate_time_difference(self):
        return 10

    def to_dict(self):
        return {
            'operator': self.operator,
            'timesheet_date': self.timesheet_date,
            'projectId': self.projectId,
            'projects': self.projectId,            
            'sub_tasks': self.sub_taskId,
            'unit_name': self.unit_name,
            'sub_unit_name': self.sub_unit_name,
            'start_chainage': self.start_chainage,
            'end_chainage': self.end_chainage,
            'task_status': self.task_status,
            'type_feature': self.type_feature,
            'type_task': self.type_task,
            'comments': self.comments,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'status': self.status,
            'id': self.id
        }   