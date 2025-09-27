from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    pipeline,
)

MODEL_NAME = "bvanaken/clinical-assertion-negation-bert"

# Load once at startup
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)


def predict(sentence: str):
    """Run inference on a sentence and return label + score"""
    result = classifier(sentence)[0]
    return {
        "label": result["label"],
        "score": round(float(result["score"]), 4),
    }
