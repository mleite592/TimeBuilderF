from peewee import Model, CharField, DateField
from database.database import BaseModel

class TimesheetStatus(BaseModel):
    operator = CharField(null=True)
    timesheet_date = DateField(null=True)
    status = CharField(null=True, default="Enabled")