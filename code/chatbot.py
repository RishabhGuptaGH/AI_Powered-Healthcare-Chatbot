#OLLAMA CONNECTION

import requests

def ask_llama3(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False  # Set to True if you want streaming output
    }
    response = requests.post(url, json=payload)
    if response.ok:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}"

# Example usage
reply = ask_llama3("Translate 'Good morning' into Spanish, Hindi, and Japanese.")
print(reply)

