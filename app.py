from fastapi import FastAPI, HTTPException
from schema.user_input import UserInput
from schema.prediction_response import PredictResponse
from model.predict import predict_output, model, model_version
import pandas as pd


app = FastAPI(
    title="Insurance Premium Prediction API",
    description="Predicts insurance premium category (Low / Medium / High) from user profile.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Insurance Premium Prediction API"}


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "model_version": model_version,
        "model_loaded": model is not None,
    }


@app.post("/predict", response_model=PredictResponse)
def predict(data: UserInput):
    user_input = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,
    }])

    try:
        return predict_output(user_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

