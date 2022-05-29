from flask import Flask, request, url_for, redirect, render_template
import keras
from keras.models import load_model
import numpy as np

app = Flask(__name__)

model=load_model("model.h5") 


@app.route("/")
def hello_world():
    return render_template('forest.html')


@app.route("/output",methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[int_features]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    print(prediction)
    output='{0:.{1}f}'.format(prediction[0][0], 2)
    print(output)
    if output>str(0.5):
        return render_template("forest.html",pred='You might be at risk.\nProbability of Cancer is {}'.format(output),bhai="Please get a proper consultation")
    else:
        return render_template("forest.html",pred='You are safe.\n Probability of Cancer is {}'.format(output),bhai="Connsultation is not needed")

if __name__ == '__main__':
    app.run(debug=True)
