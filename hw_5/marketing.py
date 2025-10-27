import requests
import json

url = 'http://localhost:9696/predict'

with open('customer.json', 'r') as f:
    customer = json.load(f)

for key in customer.keys():
    response = requests.post(url, json=customer[key])
    converted = response.json()

    print(f"{key}: {converted['churn']}, probability: {converted['churn_probability']:.4f}")
