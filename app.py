from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello')
def hello_world_2():  # put application's code here
    return '<h1>Hello World! flaskProject2</h1>'


if __name__ == '__main__':
    app.run()
