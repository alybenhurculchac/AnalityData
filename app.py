import pandas as pd
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

from flask import Flask

def showPrediction(argument):
  switcher = {
    0: "nn: Iris setosa",
    1: "nn: Iris versicolor",
    2: "nn: Iris virginica"
  }
  return (switcher.get(argument, "Unknown flower"))
    
app = Flask(__name__)

@app.route("/")
def index():
    dataset = pd.read_csv('r08iris.csv', delimiter=",")
#dividir el dataset
    X = dataset.iloc[:, 0:4].values
    y = dataset.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    clf = MLPClassifier(activation="relu",random_state=1, solver="lbfgs", max_iter=200).fit(X_train, y_train)
   
    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'wb') as file:
      pickle.dump(clf, file)
      
    # flor = clf.predict([[5.1, 3.8, 1.5, 0.3]])
    # Pre = showPrediction(flor[0])
    #y_pred = clf.predict(X_test)
    #html = """<p>>%s</p>""" % y_pred
    return "hola"


if __name__ == '__main__':
    app.run(port=5000)
