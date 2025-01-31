from flask import Blueprint, render_template

tasks_route = Blueprint('tasks', __name__)

@tasks_route.route('/')
def home():
    return render_template('index.html')
