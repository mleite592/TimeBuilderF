from flask import Blueprint, flash, redirect, render_template, request, url_for
from database.models.project import Project, Project2
from forms.project import ProjectForm

projects_route = Blueprint('projects', __name__)

@projects_route.route('/')
def index():
    projects = Project.getAll()
    print(projects)
    form = ProjectForm()
    return render_template('project_form.html', projects=projects, form = form)

@projects_route.route('/save', methods=['POST'])
def save():    
    form = ProjectForm()              
    id = form.id.data
    if form.validate_on_submit(): 
        if id:
            project = Project.get_by_id(id)
            if project:            
                project.projectCode = form.projectCode.data
                project.projectName = form.projectName.data               
                project.status = form.projectStatus.data                
                project.update()
            else:
                flash('Project not found', "error")
        else:
            new_project = Project(projectCode=form.projectCode.data, 
                                  projectName=form.projectName.data,
                                  status = form.projectStatus.data)    

            new_project.add()                    
            flash('Project created', "success")
        return redirect(url_for('projects.index'))
    
@projects_route.route('/edit/<int:id>')
def edit(id):
    projects = Project.getAll()   
    project = Project.get_by_id(id)
    form = ProjectForm(obj=project)             
    return render_template('project_form.html', projects=projects, form=form)

@projects_route.route('/delete')
def delete():
    pass