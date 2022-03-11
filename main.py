from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import joblib


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/", methods=['GET','POST'])
def main():

    if request.method == "POST":

        clf = joblib.load("clf.pkl")

        sqft = request.form.get("sqft")
        homevalue = request.form.get("homevalue")

        X = pd.DataFrame([[sqft, homevalue]], columns = ["median_square_feet", "average_listing_price"])
        prediction = clf.predict(X)[0]
    else:
        prediction = ""


    return render_template("index.html", output = prediction)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
