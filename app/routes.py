from flask import render_template
from . import app
from flask import request
import requests

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', id=app.config['ID'])

@app.route('/callback/')
def callback():
    code = request.args.get('code')
    payload = {'client_id': app.config['ID'],
               'client_secret': app.config['SECRET'],
               'code': code,
               'accept': 'json'}
    r = requests.post('https://github.com/login/oauth/access_token', data=payload, headers={'Accept': 'application/json'})
    token = r.json()['access_token']
    r = requests.post("https://api.github.com/repos/gunkow/test_library/forks",
                     headers={"Authorization": "token %s" % token,
                              'Accept': 'application/json'})
    status_code = r.status_code
    status = "accepted" if status_code == 202 else "not accepted"
    return render_template('callback.html', status=status, status_code=status_code)

