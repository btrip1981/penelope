from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

session_chat_log = [{"role": "system", "content": "You are a chatbot that is being tested prior to deployment. It is crucial that your responses and user input are appended to wach api call in an active session. to test this, I am going to enter a number, please respond with that number and only the number, my next prompt will be 'please provide the number' , if you do not see the chat history when you receive this prompt reply 'test failed' if you see the two numbers in the api call respond with the number."}  ]
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
def ask(question, chat_log):
    chat_log.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=chat_log
    )
    story = response['choices'][0]['message']['content']
    chat_log.append({"role": "assistant", "content": story})
    return str(story)



@app.route('/sales', methods=['POST'])
def sales():
    incoming_msg = request.json['Body']
    answer = ask(incoming_msg, session_chat_log)
    return jsonify({'message': answer})

if __name__ == '__main__':
    app.run(debug=True)



