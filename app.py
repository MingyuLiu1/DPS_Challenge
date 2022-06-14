from flask import Flask, render_template, request
from pyrsistent import m
import jsonify
import requests
import pickle
import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = joblib.load('dps_model.pkl')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        cat = int(request.form.get('Categoty'))
        type = int(request.form.get('Type'))
        y= int(request.form['Year'])
        m = int(request.form['Month'])
        features = [[cat, type, y, m]]
        prediction = int(model.predict(features)[0])
        # date = str(y) + '-' + str(m)
        # date = pd.to_datetime(date, format='%Y-%m')
        # prediction = model.loc[date]['forecast']
        output = round(prediction,2)
        return render_template('index.html',prediction_text=f"prediction : {output}")
        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


