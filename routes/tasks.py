from flask import Blueprint, render_template
from database.models.task import Task

tasks_route = Blueprint('tasks', __name__)

@tasks_route.route('/')
def getTasks():
    tasks = Task.select()
    return render_template('task.html', tasks = tasks)
