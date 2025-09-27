from fastapi import FastAPI
from app.model import predict
from app.schemas import SentenceInput, PredictionOutput

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionOutput)
def get_prediction(input: SentenceInput):
    return predict(input.sentence)
