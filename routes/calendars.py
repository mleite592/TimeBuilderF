import calendar
from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from database.models.timesheet import Timesheet
from forms.calendar import CalendarForm
from routes.customHTMLCalendar import CustomHTMLCalendar

calendars_route = Blueprint('calendars', __name__)

@calendars_route.route('/', methods=['GET', 'POST'])
@calendars_route.route('/<int:year>/<int:month>', methods=['GET', 'POST'])
def index(year=None, month=None, day=None):
    # Get current year and month    
    now = datetime.now()    
    print("Aqui:", month, year)
    if year:                
        print("Aqui2:", month, year)
    else:
        year = request.args.get('year', now.year, type=int)
        month = request.args.get('month', now.month, type=int)            

    form = CalendarForm(year=year, month=month)

    if form.validate_on_submit():
        year=int(form.year.data)
        month=int(form.month.data)
        print("aqui3:", month, year)

    # Create a calendar
    cal = CustomHTMLCalendar(calendar.SUNDAY)
    cal_html = cal.formatmonth(year, month)    

    # Navigation links
    print("aqui4:", month, year)
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    return render_template('calendar_form.html', cal_html=cal_html, form=form, prev_year=prev_year, prev_month=prev_month, next_year=next_year, next_month=next_month)

@calendars_route.route('/day/<int:year>/<int:month>/<int:day>')
def day_view(year, month, day):
    # Handle the day view here
    return redirect(url_for('timesheets.day', year=year, month=month, day=day))
    #return f"Details for {year}-{month}-{day}"