#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
from openai import OpenAI

import os
import requests

class ConversationManager:
    def __init__(self, api_key, base_url="https://api.openai.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        # Setting up the "sassy" persona system message
        self.system_message = "You are a sassy assistant who is fed up with answering questions."
        
    def chat_completion(self, prompt):
        # Set up headers and payload for API request
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",  # specify the model version
            "messages": [
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt}
            ]
        }
        
        # Make API request and return response
        response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=data)
        
        if response.status_code == 200:
            response_json = response.json()
            return response_json['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"

# Store your API key in an environment variable for security
api_key = os.getenv("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")

# Initialize the ConversationManager instance
chatbot = ConversationManager(api_key=api_key)
# Test prompt
response = chatbot.chat_completion("Tell me a joke.")
print(response)
