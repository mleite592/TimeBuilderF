from flask import Blueprint, flash, redirect, render_template, request, url_for
from database.models.project import Project
from forms.project import ProjectForm

projects_route = Blueprint('projects', __name__)

@projects_route.route('/')
def index():
    print("sssss") 
    projects = Project.select()
    form = ProjectForm(acton='add')
    return render_template('project_form.html', projects=projects, form = form)

@projects_route.route('/save', methods=['POST'])
def save():    
    form = ProjectForm()              
    id = form.id.data
    if form.validate_on_submit(): 
        if id:
            project = Project.get_by_id(id)
            if project:
                #project.update(
                project.projectCode = form.projectCode.data
                project.projectName = form.projectName.data               
                project.status = form.projectStatus.data                
                project.save()
            else:
                flash('Project not found')
        else:
            new_project = Project(projectCode=form.projectCode.data, 
                                  projectName=form.projectName.data,
                                  status = form.projectStatus.data)    

            new_project.save()                    
        return redirect(url_for('projects.index'))
    
@projects_route.route('/edit/<int:id>')
def edit(id):
    projects = Project.select()    
    project = Project.get_by_id(id)
    form = ProjectForm(obj=project)         
    #print("edit", form, project, id)
    return render_template('project_form.html', projects=projects, form=form)


#
#@projects_route.route('/x')
#def indexx():
#    projects = Project.select()
#    form = ProjectForm()    
#    return render_template('project_form.html', projects=projects, form = form)


@projects_route.route('/delete')
def delete():
    pass