from flask import Flask,request,jsonify
import requests
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {"Authorization": "Bearer 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"}  

def get_chatbot_response(user_input):
    payload = {"inputs": user_input}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        result = response.json()
        chatbot_response = result['generated_text'].strip()
        return chatbot_response
    else:
        return f"Error: {response.status_code}, {response.text}"

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('user_input', '')
    chatbot_response = get_chatbot_response(user_input)
    return jsonify({'chatbot_response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
