import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    dataset = pd.read_csv('r08iris.csv', delimiter=",")
#dividir el dataset
    X = dataset.iloc[:, 0:4].values
    y = dataset.iloc[:, -1].values
    return "Hello Medium"


if __name__ == '__main__':
    app.run(port=5000)
