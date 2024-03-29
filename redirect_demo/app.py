from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/')
def login():
    return '登陆界面！！'


@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '个人中心界面'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
