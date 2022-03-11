from flask import flask, request, render_template
import pandas as pd
import numpy as np
from sk.learn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    dataset = pd.read_csv("haus_me-model.csv")
    x = dataset.iloc[:. :-1].values
    y = dataset.iloc[:, -1:].values
    regressor=RandomForestClassifier(n_estimators=50, random_state=0)

    if request.method == 'POST':
        sqft = request.form.get('sqft')
        homevalue = request.form.get('home value')
        values = ([sqft, homevalue])
        result = regressor.predict(values)[0]
        if result == 1:
            output = "Based on our analysis, this house is a good deal. Buy now"
        else:
            output = "Based on our analysis, this house is not a good deal. Pass"
        
    return render_template("index.html", prediction_text = output)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
