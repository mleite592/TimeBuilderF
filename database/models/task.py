from peewee import Model, CharField
from sqlalchemy import Column, Integer, String
from database.database import BaseModel, BaseSQL


class Task2(BaseModel):
    task = CharField()
    status = CharField()

#ToDO Migrate Task to Task2

class Task(BaseSQL.Base):
    __tablename__ = 'tasks'
    id = id = Column(Integer, primary_key=True)
    task_name = Column(String)    
    status = Column(String)

    def getAll():
        tasks = BaseSQL.session.query(Task).all()
        return tasks
    
    def add(self):
        BaseSQL.session.add(self)
        BaseSQL.session.commit()

    def get_by_id(id):
        return BaseSQL.session.query(Task).filter_by(id=id).first()
    
    def get_by_task_name(task_name):
        return BaseSQL.session.query(Task).filter_by(task_name=task_name).first()

    def update(self):
        BaseSQL.session.commit()
