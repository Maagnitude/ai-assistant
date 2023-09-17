import openai
from creds import openai_key

# PAID FEATURE

class Chatbot:
    def __init__(self):
        openai.api_key = openai_key
        self.messages = []
        self.completion = None
        self.chatbot = None
        
    def generate_response(self, user_question):
        self.messages.append({"role": "user", "content": user_question})
        self.completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages, max_tokens=200, stop=None)
        msg = self.completion.choices[0].message.content
        self.messages.append(self.completion.choices[0].message)
        return msg
    
    def reset(self):
        self.messages = []
        self.completion = None
        self.chatbot = None