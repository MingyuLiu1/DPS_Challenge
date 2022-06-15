from flask import Flask, render_template, request
from pyrsistent import m
import requests
import pickle
import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

app = Flask(__name__, template_folder='templates')
model = joblib.load('dps_model.pkl')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


# standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        ym = int(request.form['YearMonth'])
        features = [[ym]]
        prediction = int(model.predict(features))
        output = round(prediction,2)
        return render_template('index.html',prediction_text=f"prediction : {output}")
        
    else:
        return render_template('index.html')
    
@app.route("/api/predict", methods=["POST"])
def apiPredict(): 
    data = request.get_json()

    ym = int(data['YearMonth'])
    if not (ym):
        return {"Error": "year or month is missing"}, 400
    elif ym < 202101:
        return {"Error": "YearMonth should be greater than 2021"}, 400

    features = [[ym]]
    prediction = int(model.predict(features)[0])

    return {'Prediction': prediction}

if __name__=="__main__":
    app.run(debug=True)


