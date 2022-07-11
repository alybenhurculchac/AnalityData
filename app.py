from flask import Flask
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Medium"


if __name__ == '__main__':
    app.run(port=5000)
