from flask import Flask
from markupsafe import escape
from flask import render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from datetime import datetime

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


@app.route('/aapost/<int:post_id>')
def show_post(post_id):
    # show an example of receiving one parameter in the URL, the param is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    # endpoint http://localhost:5000/path/a/b/c will return: Subpath a/b/c
    return f'Subpath {escape(subpath)}'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/index1')
def index1():
    return render_template('index1.html')


posts = [{'id':0, 'title': 'First Post', 'content': 'Content for the first post', 'created': '2023-01-31 10:04'}]


def get_post(post_id):
    # conn = get_db_connection()
    # post = conn.execute('SELECT * FROM posts WHERE id = ?',
    #                     (post_id,)).fetchone()
    # conn.close()
    post = posts[post_id]
    if post is None:
        abort(404)
    return post


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/')
def index():
    # posts = [{'id':1, 'title': 'First Post', 'content': 'Content for the first post', 'created': '10:04'}]
    return render_template('index.html', posts=posts)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        the_id = len(posts)
        current_date_and_time = datetime.now()

        if not title:
            flash('Title is required!')
        else:
            # conn = get_db_connection()
            # conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
            #              (title, content))
            # conn.commit()
            # conn.close()
            posts.append({'id':the_id, 'title': title, 'content': content, 'created': current_date_and_time})
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run()
