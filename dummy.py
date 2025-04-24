import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in your .env file")

# Gemini ListModels endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

# Send GET request
response = requests.get(url)

# Check and print results
if response.status_code == 200:
    data = response.json()
    for model in data.get("models", []):
        print(f"- ID: {model['name']} | Description: {model.get('description', 'No description')}")
else:
    print(f"Error {response.status_code}: {response.text}")