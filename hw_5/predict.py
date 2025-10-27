import pickle
from fastapi import FastAPI
from typing import Any

app = FastAPI(title="conversion-prediction")


def load_model(model_path):
    with open(model_path, 'rb') as f_in:
        pipeline = pickle.load(f_in)
    return pipeline


def predict_single(customer, pipeline):
    result = pipeline.predict_proba(customer)[0,1]

    return result

@app.post("/predict")
def predict(customer: dict[str, Any]):
    pipeline = load_model('pipeline_v1.bin')
    converted = predict_single(customer, pipeline)

    return {
        'churn_probability': float(converted),
        'churn': bool(converted >= 0.5)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696) # run on local host and on port 969
