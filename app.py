# app.py
from flask import Flask, render_template, request, jsonify
import anthropic
import os

app = Flask(__name__)

# Initialize Anthropic client
# Replace with your actual API key
client = anthropic.Client(api_key='YOUR_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        
        # Create a message with Claude
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": user_message
            }]
        )
        
        # Extract the response
        response = message.content[0].text
        
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)