from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):    
    projectCode = StringField('projectCode')
    projectName = StringField('projectName')
    projectStatus = SelectField('Status', choices=['enabled', 'disabled'], validators=[DataRequired()])    
