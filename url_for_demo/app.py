from flask import Flask, url_for, request

app = Flask(__name__)

# / => hello_world  路由正向视图函数
# hello_world => /  视图函数反转路由


@app.route('/')
def hello_world():
    return url_for('login', next='/')


@app.route('/list/<page>/')
def my_list(page):
    return 'my_list'


@app.route('/login/')
def login():
    next = request.args.get('next')
    return 'login'


if __name__ == '__main__':
    app.run()
