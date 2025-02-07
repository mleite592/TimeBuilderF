from peewee import Model, CharField
from database.database import BaseModel

class ProjectTasks(BaseModel):
    projectId = CharField()
    taskId = CharField()
    status = CharField()