from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import DateField, HiddenField, SelectField, StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class CalendarForm(FlaskForm):
    year = HiddenField('year')
    month = HiddenField('month')