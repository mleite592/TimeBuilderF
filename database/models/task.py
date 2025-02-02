from peewee import Model, CharField
from database.database import BaseModel


class Task(BaseModel):
    task = CharField()
    status = CharField()