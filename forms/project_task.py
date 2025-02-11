from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class ProjectTasksForm(FlaskForm):    
    projectId = HiddenField('projectId')
    tasks = SelectField('tasks', choices=[], validate_choice=False)
    taskId = HiddenField('taskId')
    status = HiddenField('status')    
    #id = IntegerField()
    id = HiddenField('ID')


