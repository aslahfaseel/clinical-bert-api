from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

MODEL_NAME = "bvanaken/clinical-assertion-negation-bert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def predict(sentence: str):
    result = classifier(sentence, truncation=True)[0]
    return {"label": result["label"], "score": round(result["score"], 4)}
