from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "Fraud Detection API"}

@app.post("/predict")
def predict(data: dict):

    features = [[
        data["amount"],
        data["country"],
        data["device"]
    ]]

    prediction = model.predict(features)

    return {"fraud": int(prediction[0])}