from flask import Blueprint, render_template, request

timesheets_route = Blueprint('timesheets', __name__)

"""
Timesheet routes
  - /projects/ (GET) - Project list
  - /projects/ (POST) - New project
  - /projects/new (GET) - Render empty project form
  - /projects/<id> (GET) - get project data
  - /projects/<id>/edit (GET) - Render project form with project data
  - /projects/<id>/ (PUT) - update project data
  - /projects/<id> (DELETE) - Delete project
"""

@timesheets_route.route('/')
def getTimesheets():    
    return render_template('timesheet.html')
