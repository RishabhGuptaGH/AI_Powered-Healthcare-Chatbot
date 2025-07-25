#OLLAMA CONNECTION
from requirements import *

def ask_llama3(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False  
    }
    response = requests.post(url, json=payload)
    if response.ok:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}"
