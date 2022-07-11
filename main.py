import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)
@app.route('/')
def anality_page():
  return "hola mundo"

