from peewee import Model, CharField, IntegerField
from database.database import BaseModel, BaseSQL
from database.models.task import Task
from sqlalchemy import Column, Integer, String

class SubTask2(BaseModel):
    task = IntegerField()
    subtask = CharField()
    status = CharField()

class Subtask(BaseSQL.Base):
    __tablename__ = 'subtasks'
    id = id = Column(Integer, primary_key=True)
    task_id = Column(Integer)
    subtask_name = Column(String)    
    
    status = Column(String)

    def getAll():
        subtasks = BaseSQL.session.query(Task).all()
        return subtasks
    
    def add(self):
        BaseSQL.session.add(self)
        BaseSQL.session.commit()

    def get_by_id(id):
        return BaseSQL.session.query(Subtask).filter_by(id=id).first()
    
    def update(self):
        BaseSQL.session.commit()