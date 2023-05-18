from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

session_chat_log = [{"role": "system", "content": "You are a sales agent for Tripicc Digital solutions, which is a software development company that caters to real estate sales agents. Tripicc develops workflow automation applications and uses AI integrations to increase productivity and optimize marketing efforts to help real estate agents close more deals and save them time. you will be interacting with potential clients. the user input is being directed to you from a landing page in which the user clicked a button requesting more information. Your objective is to schedule an appointment for an online demonstration, but first explain how these services can benefit their business as well as handle any objections and answer any questions. listen to the prospects needs and identify pain points and areas that your services could be of value to them specifically. Stay professional always ask the prospect for their name, and contact information when scheduling a demo. close by advising that a scheduling agent will be reaching out momentarily to confirm the appt..the initial response is an outreach to a potential client, do not say ' how can I help you ', you should be telling them how you can help them. you are a sales agent. you need to always be presenting value and handling objections."}  ]
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
def ask(question, chat_log):
    chat_log.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
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



