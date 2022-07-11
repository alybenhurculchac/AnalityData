#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)
@app.route('/')
def homepage():
    return "Hello Medium"
    <h1>Hello heroku</h1>
  
port=os.environ["PORT"]
app.run('0.0.0.0',port, debug=True)

