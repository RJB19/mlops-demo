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


# Triggering CI/CD workflow test at 2026-03-08