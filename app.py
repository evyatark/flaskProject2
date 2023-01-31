from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/h')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello2')
def hello_world_2():  # put application's code here
    return '<h1>Hello World! flaskProject2</h1>'


@app.route('/user/<username>')
def show_user_profile(username):
    # show an example of receiving one parameter in the URL
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show an example of receiving one parameter in the URL, the param is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    # endpoint http://localhost:5000/path/a/b/c will return: Subpath a/b/c
    return f'Subpath {escape(subpath)}'


# https://flask.palletsprojects.com/en/2.2.x/quickstart/#http-methods
# @app.get('/login')
# def login_get():
#     return show_the_login_form()
#
#
# @app.post('/login')
# def login_post():
#     return do_the_login()





@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
