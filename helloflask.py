from flask import *
import decorators

flaskApp = Flask(__name__)

decs = decorators.MyDecorators()


@flaskApp.route('/')
@decs.italify
def hello_world():
    return '<b>Hello from flask</b>'


@flaskApp.route('/Index')
def index():
    return '<b>This is Index</b>'


@flaskApp.route('/wisher/<user_name>')
def wisher(user_name):
    return f'<b>Hello {user_name} This is wisher 23</b>'


@flaskApp.route('/getbyid/<int:user_id>')
def find_by_id(user_id):
    return f'<b> This is user {user_id}</b>'


@flaskApp.route('/loadhtml')
def load_html():
    return render_template('myhtml.html')


if __name__ == '__main__':
    flaskApp.run(debug=True)
