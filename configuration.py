
from routes.home import home_route
from routes.projects import projects_route
from database.database import db
from database.models.project import Project

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(projects_route, url_prefix='/projects')

def configure_db():
    db.connect()
    db.create_tables([Project])