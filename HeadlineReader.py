from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/HeadlineReader")

def get_headlines():
    user_pass_dict = {'user': 'USER_NAME',
                    'passwd': 'PASSWORD',
                    'api_type': 'json'}
    session = requests.Session()
    session.headers.update({'User-Agent': 'Testing an alexa skill'})
    session.post('https://www.reddit.com/api/login',data = user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/technology/.json?limit=10'
    html = session.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '...'.join([i for i in titles])
    return titles

@app.route('/')
def homepage():
    return "Random homepage"

@ask.launch
def start_skill():
    welcome_message = 'Hey, would you like todays headlines'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_message = 'Todays headlines are {}'.format(headlines)
    return statement(headline_message)

@ask.intent("NoIntent")
def no_intent():
    goodbye = "Okay then. Invoke me again if you need me."
    return statement(goodbye)

if __name__ == '__main__':
    app.run(debug=True)
