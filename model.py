import joblib
import pandas as pd
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("haus_me-model.csv")
X = df[["median_square_feet", "average_listing_price"]]
y = df[["indicator"]]
clf = GaussianNB()

clf.fit(X, y)
joblib.dump(clf, "clf.pkl")

