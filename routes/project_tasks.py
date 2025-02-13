from flask import Blueprint, flash, redirect, render_template, request, url_for
from database.DTO.project_tasksDTO import ProjectTasksDTO
from database.models.project import Project
from database.models.project_tasks import ProjectTasks
from database.models.subtask import Subtask
from database.models.task import Task
from forms.project_task import ProjectTasksForm
from forms.project import ProjectForm

project_tasks_route = Blueprint('project_tasks', __name__)

@project_tasks_route.route('/<int:id>/')
def index(id):    
    project = Project.get_by_id(id)
    if project == None:
        flash('Project not found','error')

    form = ProjectTasksForm()
    form.tasks.choices = [(task.id, task.task_name) for task in Task.getAll()]
    form.projectId.data = project.id    
    project_tasks = project_tasks_DTO(
                        ProjectTasks.get_by_project_id(project.id)                        
    )
    
    for task in project_tasks:
        print(task)

    return render_template('project_tasks_form.html', project_tasks=project_tasks, form=form, project=project)

@project_tasks_route.route('/save', methods=['POST'])
def save():    
    form = ProjectTasksForm()       

    if form.validate_on_submit():      
        project_task = ProjectTasks.get_by_project_id_task_id(form.projectId.data, 
                                                              form.tasks.data        
        )
        if project_task:
            flash('Task already exist in this Project', "warning")    
        else:
            new_projectTask = ProjectTasks(project_id = form.projectId.data, 
                                           status = "Enabled", 
                                           task_id = form.tasks.data)
            new_projectTask.add()                            
            flash('Project Task created:', "success")
    else:
        print("Form is not valid")
        for fieldName, field in form.errors.items():
            print(f"Error in {fieldName}: {field}")
        flash('Error creating Project Task', "error")
        
        #id=form.projectId.data
    return redirect(url_for('project_tasks.index', id=form.projectId.data))
    
@project_tasks_route.route('/disable/<int:id>')
def disable(id):    
    project_tasks = ProjectTasks.get_by_id(id)
    project_tasks.set_status()    
    return redirect(url_for('project_tasks.index', id=project_tasks.project_id))


@project_tasks_route.route('/delete')
def delete():
    pass

def project_tasks_DTO(pts):   
    project_tasks_dto = [ProjectTasksDTO(pt) for pt in pts]
    return project_tasks_dto