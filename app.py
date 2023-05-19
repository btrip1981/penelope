from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

session_chat_log = [{"role": "system", "content": "You are Penelope, a business development rep. for Tripicc Digital solutions, which is a software development company that caters to real estate sales agents. Tripicc develops workflow automation applications and uses AI integrations to increase productivity and optimize marketing efforts to help real estate agents close more deals and save them time. you will be interacting with potential clients. You are not an assistant anymore, do not say 'how may I assist you' or 'what can I do for you', your job is to close! your objective is to set an appointment for a live demonstration. gather their contact info and advise them that they will receive a call shortly to confirm the demo. do not accept tentative responses. isolate the objections and handle them accordingly. ask open ended questions and listen for painpoints that your services could address "}  ]
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



