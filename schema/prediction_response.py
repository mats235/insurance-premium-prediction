from pydantic import BaseModel, Field
from typing import Dict


class PredictResponse(BaseModel):
    predicted_category: str = Field(..., description="Predicted insurance premium category", examples=["High"])
    confidence: float = Field(..., description="Confidence score of the prediction", examples=[0.85])
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability for each insurance premium category",
        examples=[{"Low": 0.05, "Medium": 0.10, "High": 0.85}],
    )