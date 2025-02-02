from peewee import Model, CharField
from database.database import BaseModel


class Project(BaseModel):
    projectCode = CharField()
    projectName = CharField()