# Clinical BERT API

## Project Overview
This project deploys a **Hugging Face clinical assertion BERT model** as a REST API using **FastAPI**.  
The API classifies sentences in clinical notes with labels like `PRESENT`, `ABSENT`, or `CONDITIONAL`, along with a confidence score.  

**Model used:** `bvanaken/clinical-assertion-negation-bert`  

Endpoints:
- `GET /health` – Health check
- `POST /predict` – Predict assertion status for a clinical sentence

---

## Setup Instructions (Local Development)

### Prerequisites
- Python 3.12+
- pip
- Docker 

### Install dependencies
```bash
git clone <your-github-repo-url>
cd clinical-bert-api
python -m venv venv
source venv/bin/activate   
pip install -r requirements.txt


Health check:

curl http://127.0.0.1:8000/health


Prediction:

curl -X POST http://127.0.0.1:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"sentence": "The patient denies chest pain."}'

```bash

aws ecr create-repository --repository-name clinical-bert-api
docker tag clinical-bert-api:latest <your-aws-account>.dkr.ecr.us-east-1.amazonaws.com/clinical-bert-api:latest
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-aws-account>.dkr.ecr.us-east-1.amazonaws.com
docker push <your-aws-account>.dkr.ecr.us-east-1.amazonaws.com/clinical-bert-api:latest
```

###Example API Usage (Python)

import requests

url = "http://54.226.206.113:8000/predict"
payload = {"sentence": "The patient denies chest pain."}

response = requests.post(url, json=payload)
print(response.json())
# Output: {'label': 'ABSENT', 'score': 0.9739}


##Known Issues / Tradeoffs

The API currently supports short clinical sentences (<500ms per request). Large text may slow down.

Model downloads once during startup; initial container start may take longer due to model loading.

Endpoint exposed publicly; no authentication implemented.


