from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Retrieve the API key from the environment variable
HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

# Function to call Hugging Face API
def get_hf_chatbot_response(user_query):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    data = {"inputs": user_query}

    response = requests.post(HF_MODEL_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return "Error: Unable to fetch response."

# Serve index.html as the homepage
@app.route("/")
def home():
    return render_template("index.html")  # Ensure index.html is in the "templates" folder

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get("query", "")
    response = get_hf_chatbot_response(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
