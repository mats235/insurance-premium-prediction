import pickle
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH", "model/model.pkl")
model_version = os.getenv("MODEL_VERSION", "1.0.0")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    input_df = pd.DataFrame(user_input)
    predicted_class = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs,
    }
