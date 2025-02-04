from flask import Blueprint, redirect, render_template, request, url_for
from database.models.project import Project
from forms.project import ProjectForm


projects_route = Blueprint('projects', __name__)

@projects_route.route('/')
def index():
    projects = Project.select()
    form = ProjectForm()    
    return render_template('project_form.html', projects=projects, form = form)

@projects_route.route('/project', methods=['GET', 'POST'])
@projects_route.route('/project/<int:id>', methods=['GET', 'POST'])
def project(id=None):
    if id:
        project = Project.get_by_id(id)
        form = ProjectForm(obj=project)
        if form.validate_on_submit():
            project.update(                
                projectCode = form.projectCode.data,
                projectName = form.projectName.data,               
                projectStatus = form.projectStatus.data
            )
            print("Saved", project.projectCode, project.projectName)            
            return redirect(url_for('projects.index'))
    else:
        form = ProjectForm()
        if form.validate_on_submit():
            new_project = Project(projectCode=form.projectCode.data, projectName=form.projectName.data)
            #db.session.add(new_project)
            #db.session.commit()
            print("Saved3")
            return redirect(url_for('projects.index'))        
    # refresh records
    projects = Project.select()    
    return render_template('project_form.html', form=form, id=id, projects= projects)

@projects_route.route('/edit/<int:id>')
def edit_project(id):
    project = Project.get_by_id(id)
    form = ProjectForm(obj=project)     
    print("edit", id)
    return render_template('project_form.html', form=form, id=id)


@projects_route.route('/delete/<int:id>')
def delete_project(id):
    form = ProjectForm()    
    projects = Project.select()    
    #delete
    #projects = Project.delete_by_id(id)
    print("delete", id)
    return render_template('project_form.html', form=form, id=id, projects= projects)

