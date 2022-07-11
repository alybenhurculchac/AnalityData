import pandas as pd
from sklearn.neural_network import MLPClassifier

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Medium"


if __name__ == '__main__':
    app.run(port=5000)
