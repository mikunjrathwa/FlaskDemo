from flask import Flask

flaskApp = Flask(__name__)

flaskApp.route('/')


def hello_world():
    return 'Hello from flask'


hello_world()

