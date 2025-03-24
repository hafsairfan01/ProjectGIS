from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
CORS(app)

HF_API_KEY = os.getenv("HF_API_KEY")

# Model URL (You can change this to another model if needed)
HF_MODEL_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"


# API headers
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Input data for the model
data = {"inputs": "Hello, how are you?"}

# Send request
response = requests.post(HF_MODEL_URL, headers=headers, json=data)

# Print response
print(f"Status Code: {response.status_code}")
print("Response:", response.json())
