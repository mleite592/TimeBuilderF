
from sqlalchemy import create_engine
from database.models.project_tasks import ProjectTasks
from database.models.subtask import SubTask2, Subtask
from database.models.task import Task, Task2
from database.models.timesheet import Timesheet
from routes.home import home_route
from routes.projects import projects_route
from routes.timesheets import timesheets_route
from routes.tasks import tasks_route
from routes.subtasks import subtasks_route
from routes.calendars import calendars_route
from routes.project_tasks import project_tasks_route
from database.database import db
from database.models.project import Project
from database.models.timesheet_status import TimesheetStatus
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
import secrets
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.database import BaseSQL

def configure_all(app):
    configure_app(app)
    configure_routes(app)
    configure_db()
    configure_db_SQL()

def configure_app(app):  
    foo = secrets.token_urlsafe(16)
    app.secret_key = foo
    app.config['SECRET_KEY'] = foo        
    bootstrap = Bootstrap5(app)
    csrf = CSRFProtect(app)

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(projects_route, url_prefix='/projects')
    app.register_blueprint(timesheets_route, url_prefix='/timesheets')
    app.register_blueprint(tasks_route, url_prefix='/tasks')
    app.register_blueprint(subtasks_route, url_prefix='/subtasks')    
    app.register_blueprint(calendars_route, url_prefix='/calendars')
    app.register_blueprint(project_tasks_route, url_prefix='/project_tasks')

def configure_db_SQL():    
    # Create the books table
    engine = BaseSQL.engine
    BaseSQL.Base.metadata.create_all(engine)

def configure_db():
    db.connect()
    #db.drop_tables([Subtask])
    #db.drop_tables([Project])
    #db.create_tables([Project])
    #db.create_tables([Task])
    db.create_tables([SubTask2])
    #db.drop_tables([ProjectTasks])
    #db.create_tables([ProjectTasks])
    #db.drop_tables([Timesheet])
    #db.create_tables([Timesheet])
    #db.create_tables([TimesheetStatus])
    #migrateTask()
    #migratesubTask()
    #preLoadSubTask()

def migrateTask():
    tasks = Task.select()

    for t in tasks:
        t2 = Task2(task_name = t.task,
                       status = t.status)
        t2.add()

def migratesubTask():
    tasks = SubTask2.select()

    for t in tasks:
        t2 = Subtask(subtask_name = t.task,
                      task_id = t.task,
                       status = t.status)
        t2.add()


def preLoadTask():
    #projects = pd.read_excel("database/dataset.xlsx", sheet_name="Projects")
    tasks = pd.read_excel("database/dataset.xlsx", sheet_name="Tasks")
    #sub_tasks = pd.read_excel("database/dataset.xlsx", sheet_name="Sub-tasks")
    
    #print(tasks, sub_tasks)

    ## INSERT
    #for index, row in tasks.iterrows():
    #    Task.create(task = row.Task, status = "Enabled")
    #    #print(row.Task)

    ## QUERY
    query = Task.select()
    for record in query:
        print(record.id, record.task, record.status)

    ## DELETE
    #query = Task.delete()
    #query.execute()

def preLoadSubTask():
    #projects = pd.read_excel("database/dataset.xlsx", sheet_name="Projects")
    #tasks = pd.read_excel("database/dataset.xlsx", sheet_name="Tasks")
    subtasks = pd.read_excel("database/dataset.xlsx", sheet_name="Subtasks")
    
    #print(tasks, sub_tasks)

    ###INSERT
    for index, row in subtasks.iterrows():
        print(row.Task, row.Subtask)
        try:
            task = Task.get_by_task_name(row.Task)
            #print(task)
            print(row.Subtask, task.id)
            subtask = Subtask(
                task_id = task.id,
                subtask_name = row.Subtask,
                status = "Enabled"
            )
            ###
            ##subtask.add()
            ###
        except Task.DoesNotExist:
            print("Task not found") 

        ## QUERY
    #query = Subtask.select()
    #for record in query:
    #    print(record.id, record.subtask, record.status)

    ## DELETE
    #query = Subtask.delete()
    #query.execute()
