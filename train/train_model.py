import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/processed_dataset.csv")

X = df[["amount", "country", "device"]]
y = df["fraud"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model/model.pkl")

print("Model trained!")