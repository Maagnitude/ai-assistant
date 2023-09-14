# import openai
# from creds import openai_key

# # NOT WORKING YET

# # Set your OpenAI API key
# api_key = openai_key

# # Initialize the OpenAI API client
# openai.api_key = api_key

# # Define a function to generate a response to a user question
# def generate_response(user_question):
    
#     completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_question}])
#     text = completion.choices[0].message.content
#     return text