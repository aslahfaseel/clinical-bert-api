from pydantic import BaseModel

class SentenceInput(BaseModel):
    sentence: str

class PredictionOutput(BaseModel):
    label: str
    score: float
