from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from database.DTO.timesheetDTO import TimesheetDTO
from database.models.project_tasks import ProjectTasks
from database.models.task import Task
from database.models.timesheet import Timesheet
from database.models.project import Project
from database.models.subtask import SubTask
from forms.timesheet import TimeSheetForm
from peewee import fn
from datetime import datetime

timesheets_route = Blueprint('timesheets', __name__)

@timesheets_route.route('/')
@timesheets_route.route('/<int:id>')
@timesheets_route.route('/<int:year>/<int:month>/<int:day>')
def index(id=None, year=None, month=None, day=None):         
    
    print("Aqui:", id, year, month, day)
    if year:
        timesheet_day_selected = f'{year}-{month:02d}-{day:02d}'        
        
        timesheets = timesheetsDTO(
            Timesheet.select().where(
                (Timesheet.status != 'Deleted') &
                (Timesheet.timesheet_date == timesheet_day_selected)           
            )
        )        
        form = TimeSheetForm(timesheet_day = timesheet_day_selected)        
    else:
        flash('Timesheet date not informed')

    if id:
        form = TimeSheetForm(obj=Timesheet.get_by_id(id))                
        print("dddd")
    #else:
        #form = TimeSheetForm(timesheet_date = timesheet_day_selected)
     #   print("ddddxxxx")
    
    projects = Project.select().where(Project.status != "disabled")
    
    form.projects.choices = [(p.id, p.projectName) for p in Project.select().where(Project.status != "disabled")]

    return render_template('timesheet_form.html', timesheets=timesheets, projects=projects, form=form, year=year, month=month, day=day, timesheet_day_selected=convert_date_ymd_to_mdy(year, month, day))

#@timesheets_route.route('/save', methods=['POST'])
@timesheets_route.route('/save/<int:year>/<int:month>/<int:day>', methods=['POST'])
def save(year, month, day):    
    form = TimeSheetForm()                 

    id = form.id.data
    form.timesheet_date = convert_date_ymd_to_date(year, month, day)
    
    if form.validate_on_submit(): 
        if id:
            timesheet = Timesheet.get_by_id(id)
            if timesheet:
                #ToDO
                timesheet.save()
            else:
                flash('Timesheet not found', 'error')
        else:                      
            new_timesheet = Timesheet(timesheet_date=form.timesheet_date,
                                      operator="m.leite@fugro.com",                             
                                      status = "Open",
                                      projectId = form.projects.data,
                                      sub_taskId = form.sub_tasks.data,
                                      start_time = form.start_time.data,
                                      end_time = form.end_time.data
                                      )
            print("new", new_timesheet.timesheet_date, new_timesheet.operator, form.projects.data)                         
            try:                     
                new_timesheet.save()                
                flash('Timesheet created successfully', 'success')
            except Exception as e:
                flash(f'Error creating timesheet: {e}', 'error')            
    return redirect(url_for('timesheets.index', year=year, month=month, day=day))
    
@timesheets_route.route('/edit/<int:id>', methods=['POST'])
def edit(id):        
    timesheet = Timesheet.get_by_id(id)
    if timesheet:
        year = timesheet.timesheet_date.year
        month = timesheet.timesheet_date.month
        day = timesheet.timesheet_date.day                               
    else:
        flash('Timesheet not found', 'error')

    return redirect(url_for('timesheets.index', id=id, year=year, month=month, day=day))

#@timesheets_route.route('/delete/<int:id>/<int:year>/<int:month>/<int:day>', methods=['POST'])
#def delete(id, year, month, day):    
@timesheets_route.route('/delete/<int:id>/')
def delete(id):    
    timesheet = Timesheet.get_by_id(id)    
    if timesheet:        
        year = timesheet.timesheet_date.year
        month = timesheet.timesheet_date.month
        day = timesheet.timesheet_date.day        
        timesheet.status = "Deleted"
        timesheet.save()
        flash('Timesheet deleted successfully')
    else:
        flash('Timesheet not found')
    return redirect(url_for('timesheets.index', year=year, month=month, day=day))

@timesheets_route.route('/tasks/<int:projectId>/')
def task(projectId):
    print("A:", projectId)
    tasksquery = ProjectTasks().select().where(ProjectTasks.projectId == projectId)

    tasks = []

    for t in tasksquery:
        task = Task.get_by_id(t.id)
        taskDTO = {}
        taskDTO['id'] = task.id
        taskDTO['task'] = task.task
        tasks.append(taskDTO)

    return jsonify({'tasks': tasks})

@timesheets_route.route('/subtasks/<int:taskId>/')
def subtask(taskId):
    print("B:", taskId)
    subtasksquery = SubTask().select().where(SubTask.task == taskId)

    subtasks = []

    for t in subtasksquery:
        print(t.id)
        subtask = SubTask.get_by_id(t.id)
        
        subtaskDTO = {}
        subtaskDTO['id'] = subtask.id
        subtaskDTO['subtask'] = subtask.subtask
        print(subtaskDTO)
        subtasks.append(subtaskDTO)

    return jsonify({'tasks': subtasks})

def convert_date_ymd_to_mdy(year, month, day):
    date_obj= datetime(year, month, day)
    return date_obj.strftime('%m-%d-%Y')

def convert_date_ymd_to_date(year, month, day):
    # Format the date as "YYYY-MM-DD"
    formatted_date = f'{year:04d}-{month:02d}-{day:02d}'
    # Assign the formatted date to form.timesheet_date
    return formatted_date
    
def timesheetsDTO(timesheets):
    timesheets_dto = [TimesheetDTO(timesheet) for timesheet in timesheets]
    return timesheets_dto

def timesheetDTO(timesheet):
    timesheetDTO = TimesheetDTO(timesheet)
    return timesheetDTO