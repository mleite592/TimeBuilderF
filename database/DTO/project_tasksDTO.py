from database.models import project_tasks
from database.models.project import Project
from database.models.task import Task


class ProjectTasksDTO:
    def __init__(self, project_tasks: project_tasks):                
        #project = Project.get_by_id(project_tasks.projectId)
        task = Task.get_by_id(project_tasks.task_id)
        self.id = project_tasks.id
        self.task = task.task_name
        self.status = project_tasks.status

    def __repr__(self):
        return f'ProjectTaskDTO(id={self.id}, task={self.task}, status={self.status})'