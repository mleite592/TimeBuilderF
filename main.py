from flask import Flask, render_template
from configuration import configure_all
from flask_cors import CORS
from configuration import preLoadSubTask, preLoadTask

app = Flask(__name__)
CORS(app)  
RESPONSE_HEADERS = { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' } 

configure_all(app)

if __name__ == "__main__":    
    app.run(debug=True)


#preLoadTask()
#preLoadSubTask()
