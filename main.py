from flask import Flask, render_template
from configuration import configure_all
from configuration import preLoadSubTask, preLoadTask

app = Flask(__name__)

configure_all(app)

#preLoadTask()
#preLoadSubTask()

app.run(debug=True)