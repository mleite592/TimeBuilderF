from peewee import Model, CharField
from database.database import BaseModel
from sqlalchemy import Column, Integer, String
from database.database import BaseSQL


class ProjectTasks2(BaseModel):
    projectId = CharField()
    taskId = CharField()
    status = CharField()

class ProjectTasks(BaseSQL.Base):
    __tablename__ = 'project_tasks'
    id = id = Column(Integer, primary_key=True)
    project_id = Column(Integer)    
    task_id = Column(Integer)    
    status = Column(String)

    def getAll():
        project_tasks = BaseSQL.session.query(ProjectTasks).all()
        return project_tasks
    
    def add(self):
        BaseSQL.session.add(self)
        BaseSQL.session.commit()

    def get_by_id(id):
        return BaseSQL.session.query(ProjectTasks).filter_by(id=id).first()
    
    def get_by_project_id(projectId):
        return BaseSQL.session.query(ProjectTasks).filter_by(project_id=projectId)
    
    def get_by_project_id_task_id(project_id, task_id):
        t = BaseSQL.session.query(ProjectTasks).filter_by(project_id=project_id, task_id = task_id).first()
        print(t)
        return t
        
    def update(self):
        BaseSQL.session.commit()

    def set_status(self):        
        if self.status == "Enabled":
            self.status = "Disabled"        
        else:
            self.status = "Enabled"    
        BaseSQL.session.commit()