import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
headers = {"Authorization": "Bearer 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"}
 
print("Chatbot: Hello! Type 'exit' to end the conversation.")
def chatbot():
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        payload = {"inputs": user_input}
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            # print(result)
            chatbot_response = result['generated_text'].strip()
            print(f"Chatbot: {chatbot_response}")
        else:
            print(f"Error: {response.status_code}, {response.text}")

chatbot()