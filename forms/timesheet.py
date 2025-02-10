from typing import Optional
from flask_wtf import FlaskForm
from wtforms import DateField, HiddenField, SelectField, StringField, BooleanField, SubmitField, IntegerField, TimeField
from wtforms.validators import DataRequired, Length
from datetime import datetime, time

class TimeSheetForm(FlaskForm):    
    timesheet_date = StringField('timesheet_date')    
    projectId = HiddenField('projectId')
    projects = SelectField('projects', choices=[], validate_choice=False)
    tasks = SelectField('task', choices=[], validate_choice=False)
    sub_tasks = SelectField('subtask', choices=[], validate_choice=False)    
    unit_name = StringField('unitName', render_kw={"style": "width: 50px;"})
    sub_unit_name = StringField('subUnitName', render_kw={"style": "width: 50px;"})
    start_chainage = IntegerField('start_chainage', default=1, render_kw={"style": "width: 50px;"})
    end_chainage = IntegerField('end_chainage', default=2, render_kw={"style": "width: 50px;"})
    task_status = SelectField('task_status', default='Pending', choices=['Completed', 'Pending'], validate_choice=True ) #Completed, Pending
    type_feature = SelectField('type_feature', default='Traditional', choices=['Traditional', 'Roames'], validate_choice=True) #Traditional or Roames
    type_task =  SelectField('type_task', default='Regular', choices=['Regular', 'Rework', 'QC'], validate_choice=True)   #Regular, Rework or QC
    comments = StringField('comments')    
    start_time = TimeField('start_time', default=time(14,0), format='%H:%M')
    end_time = TimeField('end_time', default=time(15,0), format='%H:%M')
    status = StringField('Status', default='Open')
    operator = HiddenField('Operator')
    id = HiddenField('ID')

