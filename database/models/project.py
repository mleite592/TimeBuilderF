from peewee import Model, CharField
from database.database import db

class Project(Model):
    projectCode = CharField()
    projectName = CharField()

    class Meta:
        database: db
