from peewee import Model, CharField, IntegerField, DateField, DateTimeField
from database.database import BaseModel


class Timesheet(BaseModel):
    operator = CharField()
    date = DateField()
    projectId = IntegerField()    
    unit_name = CharField()
    sub_unit_name = CharField()
    sub_task = CharField()
    start_chainage = IntegerField('start_chainage')
    end_chainage = IntegerField('end_chainage')
    task_status = CharField()
    type_feature = CharField() #Traditional or Roames
    type_task =  CharField()    #Rework or QC
    comments = CharField()    
    start_time = DateTimeField()
    end_time = DateTimeField()       
    status = CharField() # Open, Submitted, Approved, Deleted