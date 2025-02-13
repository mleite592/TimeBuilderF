from peewee import Model, CharField
from sqlalchemy import Column, Integer, String
from database.database import BaseModel
from database.database import BaseSQL


class Project2(BaseModel):
    projectCode = CharField()
    projectName = CharField()
    status = CharField()

class Project(BaseSQL.Base):
    __tablename__ = 'projects'
    id = id = Column(Integer, primary_key=True)
    projectCode = Column(String)
    projectName = Column(String)
    status = Column(String)

    def getAll():
        projects = BaseSQL.session.query(Project).all()
        return projects
    
    def add(self):
        BaseSQL.session.add(self)
        BaseSQL.session.commit()

    def get_by_id(id):
        return BaseSQL.session.query(Project).filter_by(id=id).first()
    
    def update(self):
        BaseSQL.session.commit()

        
    
    