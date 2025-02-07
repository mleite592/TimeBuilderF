from typing import Optional
from flask_wtf import FlaskForm
from wtforms import DateField, HiddenField, SelectField, StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime

class TimeSheetForm(FlaskForm):
    operator = StringField('operator')    
    timesheet_date = StringField('timesheet_date')    
    projectId = StringField('projectId')
    #projectCode = SelectField('projectCode', default='None')
    #projectName = SelectField('projectName', default='None')    
    unit_name = StringField('unitName')
    sub_unit_name = StringField('subUnitName')
    #sub_task = SelectField('subtask', default='None')
    start_chainage = IntegerField('start_chainage')
    end_chainage = IntegerField('end_chainage')
    #task_status = SelectField('task_status', default='Pending') #Completed, Pending
    #type_feature = SelectField('type_feature', default='Tradiotional') #Traditional or Roames
    #type_task =  SelectField('type_task', default='Regular')   #Regular, Rework or QC
    comments = StringField('comments')    
    start_time = StringField('start_time')
    end_time = StringField('end_time')
    status = StringField('Status', default='Open')
    id = HiddenField('ID')


