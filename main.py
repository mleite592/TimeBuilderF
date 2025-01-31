from flask import Flask, render_template
from routes.home import home_route
from routes.projects import projects_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(projects_route, url_prefix='/projects')

#@app.route("/")
#def hw():
#    return render_template('home.html')

app.run(debug=True)