from peewee import Model, CharField, IntegerField
from database.database import BaseModel
from database.models.task import Task


class Subtask(BaseModel):
    task = IntegerField()
    subtask = CharField()
    status = CharField()