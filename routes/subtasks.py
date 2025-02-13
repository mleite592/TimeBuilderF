from flask import Blueprint, render_template
from database.models.subtask import Subtask
from database.models.task import Task
from database.DTO.subtaskDTO import SubtaskDTO

subtasks_route = Blueprint('subtasks', __name__)

@subtasks_route.route('/')
def getSubtasks():
    subtasks = Subtask.getAll()
    subtasks_return = []

    for s in subtasks:
        s_dto = SubtaskDTO(s.id,
                           s.subtask,
                           Task.get(Task.id == s.task).task,
                           s.status
                           )
        subtasks_return.append(s_dto)
                
    return render_template('subtask.html', subtasks = subtasks_return)
