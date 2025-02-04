from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):    
    projectCode = StringField('projectCode')
    projectName = StringField('projectName')
    projectStatus = SelectField('Status', choices=['enabled', 'disabled'], validators=[DataRequired()])    
    #id = IntegerField()
    id = HiddenField('ID')


