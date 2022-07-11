from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)
@app.route('/')
def ontology_page():
   return 

port=os.environ["PORT"]
app.run('0.0.0.0',port, debug=True)

