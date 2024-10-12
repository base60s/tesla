import json
import os
import openai  # Changed import statement

# Load the JSON file
file_path = '/Users/mauriciovelez/Desktop/TSLA-Q2-2024-Update.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract the OpenAI API key from the JSON data
api_key = "Replace with your actual OpenAI API key"  # Replace with your actual OpenAI API key

# Initialize the OpenAI client
openai.api_key = api_key  # Set the API key

def ask_question(question, context):
    response = openai.ChatCompletion.create(  # Updated method call
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about the TSLA Q2 2024 Update."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message['content']  # Updated access to response content

# Main loop for user interaction
while True:
    user_question = input("Ask a question about the TSLA Q2 2024 Update (or type 'quit' to exit): ")
    
    if user_question.lower() == 'quit':
        break
    
    answer = ask_question(user_question, json.dumps(data))
    print("\nAnswer:", answer, "\n")

print("Thank you for using the TSLA Q2 2024 Update assistant!")
