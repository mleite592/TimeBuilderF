from peewee import Model, CharField, IntegerField
from database.database import BaseModel
from database.models.task import Task


class SubTask(BaseModel):
    task = IntegerField()
    subtask = CharField()
    status = CharField()