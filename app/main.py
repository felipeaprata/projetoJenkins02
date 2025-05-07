import os
import newrelic.agent

newrelic.agent.initialize(
    license_key=os.getenv('6b47aab476d8e115219d8b2e3dd776d8FFFFNRAL'),
    app_name='Flask-CICD'
)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"