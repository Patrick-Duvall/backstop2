from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    alerts = [
        {
            'email': 'jon@test.com',
            'body': 'Beautiful day in Portland!'
        },
        {
            'email': 'pat@test.com',
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, alerts=alerts)
