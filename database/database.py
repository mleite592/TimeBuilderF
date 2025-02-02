from peewee import SqliteDatabase
from peewee import Model

db = SqliteDatabase("tb.db")

# Base model class
class BaseModel(Model):
    class Meta:
        database = db