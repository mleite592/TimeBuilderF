from peewee import SqliteDatabase
from peewee import Model
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = SqliteDatabase("tb.db")

connection_string = 'mssql+pyodbc://landmarciopoc-server-admin:LaNMarcioPoc%^&*1@landmarciopoc-server.database.windows.net:1433/landmarciopoc-database?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_string, echo=True) 
Base = declarative_base()

# Base model class
class BaseModel(Model):
    class Meta:
        database = db

class BaseSQL():
    Base = Base
    engine = engine
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()