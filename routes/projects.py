from flask import Blueprint, render_template
from database.projects import PROJECTS
from database.models.project import Project


projects_route = Blueprint('projects', __name__)

"""
Projects routes
  - /projects/ (GET) - Project list
  - /projects/ (POST) - New project
  - /projects/new (GET) - Render empty project form
  - /projects/<id> (GET) - get project data
  - /projects/<id>/edit (GET) - Render project form with project data
  - /projects/<id>/ (PUT) - update project data
  - /projects/<id> (DELETE) - Delete project
"""

@projects_route.route('/')
def getProjects():    
    projects = Project.select()
    return render_template('timesheet.html', projects = projects)

@projects_route.route('/', methods=['POST'])
def postProject():
    pass

@projects_route.route('/new')
def newProject():
    pass

@projects_route.route('/<int:project_code>')
def getProject(project_code):
    print(project_code)
    pass

@projects_route.route('/<int:project_code>/edit')
def editProject(project_code):
    print(project_code)
    pass

@projects_route.route('/<int:project_code>/update', methods=['PUT'])
def putProject():
    pass

@projects_route.route('/')
def delProject():
    pass

