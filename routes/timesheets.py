from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from database.DTO.timesheetDTO import TimesheetDTO
from database.models.project_tasks import ProjectTasks
from database.models.task import Task
from database.models.timesheet import Timesheet
from database.models.project import Project
from database.models.subtask import SubTask
from forms.timesheet import TimeSheetForm
from database.models.timesheet_status import TimesheetStatus
from peewee import fn
from datetime import datetime

timesheets_route = Blueprint('timesheets', __name__)

@timesheets_route.route('/')
@timesheets_route.route('/<int:id>')
@timesheets_route.route('/<int:year>/<int:month>/<int:day>')
def index(id=None, year=None, month=None, day=None):         
    
    if year:
        timesheet_day_selected = f'{year}-{month:02d}-{day:02d}'        
        form = TimeSheetForm()        
        form.timesheet_date.data = timesheet_day_selected

        #Fetch timesheet records        
        timesheets = timesheetsDTO(
            Timesheet.select().where(
                (Timesheet.status != 'Deleted') &
                (Timesheet.timesheet_date == timesheet_day_selected)
            )
        )        

        #Fetch timesheet status
        timesheet_status = TimesheetStatus.select().where(
                    (TimesheetStatus.operator == "m.leite@fugro.com") &
                    (TimesheetStatus.timesheet_date == timesheet_day_selected)
        ).first()

        if timesheet_status:    
            print(timesheet_status.status)
            form.status.data = timesheet_status.status
        else:
            timesheet_status = TimesheetStatus(operator = "m.leite@fugro.com",
                                               status = "Open",
                                               timesheet_date = timesheet_day_selected
                                    )
            timesheet_status.save()
            print("Create timesheetstatus")
        form.status.data = timesheet_status.status
    else:
        flash('Timesheet date not informed')

    if id:
        form = TimeSheetForm(obj=Timesheet.get_by_id(id))                        
    #else:
        #form = TimeSheetForm(timesheet_date = timesheet_day_selected)
     #   print("ddddxxxx")
    
    projects = Project.select().where(Project.status != "disabled")
        
    form.projects.choices = [("", "Select a project")] + [(p.id, p.projectName) for p in Project.select().where(Project.status != "disabled")]
    
    #form.projects.choices = [(p.id, p.projectName) for p in Project.select().where(Project.status != "disabled")]

    return render_template('timesheet_form.html', timesheets=timesheets, projects=projects, form=form, year=year, month=month, day=day, timesheet_day_selected=convert_date_ymd_to_mdy(year, month, day))

#@timesheets_route.route('/save', methods=['POST'])
@timesheets_route.route('/save/<int:year>/<int:month>/<int:day>', methods=['POST'])
def save(year, month, day):     
    print("Aqui")

    form = TimeSheetForm()
    if request.method == 'POST':
        print("Aqui2")

        if form.validate_on_submit():
            print("Aqui3", form.projects.data)
            id = form.id.data
            if id:
                timesheet = Timesheet.get_by_id(id)
                if timesheet:
                    # Update the timesheet with form data
                    timesheet.operator = form.operator.data
                    timesheet.timesheet_date = form.timesheet_date.data
                    timesheet.projectId = form.projects.data
                    #timesheet.tasks = form.tasks.data
                    timesheet.sub_taskId = form.sub_tasks.data
                    timesheet.unit_name = form.unit_name.data
                    timesheet.sub_unit_name = form.sub_unit_name.data
                    timesheet.start_chainage = form.start_chainage.data
                    timesheet.end_chainage = form.end_chainage.data
                    timesheet.task_status = form.task_status.data
                    timesheet.type_feature = form.type_feature.data
                    timesheet.type_task = form.type_task.data
                    timesheet.comments = form.comments.data
                    timesheet.start_time = form.start_time.data
                    timesheet.end_time = form.end_time.data
                    timesheet.status = form.status.data
                    timesheet.save()                    
                    flash('Timesheet updated successfully', 'success')
                else:
                    flash('Timesheet not found', 'error')
            else:
                print("Aqui:", form.sub_tasks.data)
                # Create a new timesheet
                new_timesheet = Timesheet(
                    operator=form.operator.data,
                    timesheet_date=form.timesheet_date.data,
                    projectId = form.projects.data,                                        
                    #tasks=form.tasks.data,
                    sub_taskId=form.sub_tasks.data,
                    unit_name=form.unit_name.data,
                    sub_unit_name=form.sub_unit_name.data,
                    start_chainage=form.start_chainage.data,
                    end_chainage=form.end_chainage.data,
                    task_status=form.task_status.data,
                    type_feature=form.type_feature.data,
                    type_task=form.type_task.data,
                    comments=form.comments.data,
                    start_time=form.start_time.data,
                    end_time=form.end_time.data,
                    status="Open"
                )
                new_timesheet.save()
                #return {jsonify(new_timesheet)}
                flash('Timesheet created successfully', 'success')
        else:            
           for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", "error")
                
    
    
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

@timesheets_route.route('/submit/<int:year>/<int:month>/<int:day>')
def submit(year, month, day):
    form = TimeSheetForm()

    timesheet_status = TimesheetStatus.select().where(TimesheetStatus.timesheet_date  == convert_date_ymd_to_date(year, month, day),
                                                          TimesheetStatus.operator == "m.leite@fugro.com").first()
    
    if timesheet_status:                  
        print("XX", timesheet_status.status) 
        if timesheet_status.status == "Approved":
            flash("Timesheet already approved! No changes are allowed.", "error")
        else:
            if timesheet_status.status == "Open":
                new_status = "Submitted"
            else:
                new_status = "Open"
                print("Reopening")            
            
            timesheet_status.status = new_status
            timesheet_status.save()

            #Update timesheet records        
            query = Timesheet.update(status=new_status).where(
                Timesheet.timesheet_date == convert_date_ymd_to_date(year, month, day),
                Timesheet.status != 'Deleted'
                )        
            query.execute()
            print("KKKK:", timesheet_status.status)
    else:
        flash("Timesheet status not found", "error")
                                                          
    form.status.data = new_status
    print("KSKSK:", form.status.data)
        
    return redirect(url_for('timesheets.index', year=year, month=month, day=day))


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