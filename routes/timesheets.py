from flask import Blueprint, render_template, request
from flask import Blueprint, flash, redirect, render_template, request, url_for
from database.models.timesheet import Timesheet
from database.models.project import Project
from database.models.subtask import Subtask
from forms.timesheet import TimeSheetForm

timesheets_route = Blueprint('timesheets', __name__)

@timesheets_route.route('/')
def index():     
    timesheets = Timesheet.select() ## ToDo: query by date    
    form = TimeSheetForm()
    return render_template('timesheet_form.html', timesheets=timesheets, form = form)

@timesheets_route.route('/save', methods=['POST'])
def save():    
    form = TimeSheetForm()              
    id = form.id.data
    print(form.date.data)
    if form.validate_on_submit(): 
        print("XXXX")
        if id:
            timesheet = Timesheet.get_by_id(id)  ## query by date
            if timesheet:
                timesheet.date  = form.date.date,                               
                timesheet.save()
            else:
                flash('Timesheet not found')
        else:
            new_timesheet = Timesheet(date = form.date.data                                     )    
            new_timesheet.save()                    
    return redirect(url_for('timesheets.index'))
    
@timesheets_route.route('/edit/<int:id>')
def edit(id):
    timesheets = Timesheet.select()    
    timesheet = Timesheet.get_by_id(id)
    form =Timesheet(obj=timesheet)         
    #print("edit", form, project, id)
    return render_template('timesheet_form.html', timesheets = timesheets, form=form)

@timesheets_route.route('/delete')
def delete():
    pass
