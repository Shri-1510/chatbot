# DialoGPT Chatbot

## Overview
This project implements a chatbot using the DialoGPT-medium model from Hugging Face. The chatbot allows users to interact with the model through a simple web interface.

## Components
1. **Backend (server.py):**
   - The Flask server handles incoming requests from the frontend and communicates with the Hugging Face API to get responses from the DialoGPT-medium model.
   - CORS (Cross-Origin Resource Sharing) is enabled to allow communication between the frontend and backend.

2. **Frontend (frontend.html):**
   - The HTML file provides a basic web interface for users to interact with the chatbot.
   - User input is sent to the backend API, and the chatbot's response is displayed in the chat container.

3. **Chatbot Logic (chatbot.py):**
   - The chatbot logic is responsible for interacting with the DialoGPT-medium model using the Hugging Face API.
   - It sends user input to the Hugging Face API, which in turn queries the DialoGPT-medium model to generate responses.
   - The responses are processed, and the chatbot provides coherent and context-aware replies.

## The Model: DialoGPT-medium
- DialoGPT-medium is a conversational language model developed by Microsoft, based on the GPT (Generative Pre-trained Transformer) architecture.
- Specifically fine-tuned for dialog-based applications, making it suitable for natural and dynamic conversations.

## Chatbot Logic
- The chatbot logic handles user interactions by taking user input, sending it to the DialoGPT-medium model, and retrieving the generated responses.
- Ensures context continuity by maintaining a conversation history, allowing the model to understand and respond coherently to the ongoing dialog.
- Exception handling is implemented to manage errors and unexpected responses from the Hugging Face API.

## Usage
1. **Run the Backend Server:**
   - Execute `server.py` to start the Flask server. The server runs on http://localhost:5000 by default.

     ```bash
     python server.py
     ```

2. **Open the Frontend Interface:**
   - Open the `frontend.html` file in a web browser. Interact with the chatbot through the provided input field and send messages by clicking the "Send" button.

3. **Chat with the Chatbot:**
   - Type your messages in the input field and click "Send." The chatbot will provide responses based on the DialoGPT-medium model.

4. **Exit the Chat:**
   - Type 'exit' to end the conversation and close the chatbot.

## Important Note
- Ensure that you have the necessary dependencies installed, including Flask, requests, and flask-cors.

## Configuration
- Modify the `API_URL` and `HEADERS` variables in `server.py` to use your own Hugging Face API key and model details.

## Acknowledgments
- This project leverages the DialoGPT-medium model from Microsoft and the Hugging Face API.
