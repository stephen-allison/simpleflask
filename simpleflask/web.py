from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, world from web.py"

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, {0)'.format(name)

