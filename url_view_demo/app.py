from flask import Flask,request

app = Flask(__name__)

import uuid


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/list/')
def article_list():
    return 'article list'


@app.route('/article/<int:article_id>/')
def article_detail(article_id):
    return '您请求的文章是{}'.format(article_id)


@app.route('/article/<string:article_id>/')
def article_details(article_id):
    return '您请求的文章是: {}'.format(article_id)


@app.route('/article/<path:test>/')
def test_article(test):
    return 'test article: {}'.format(test)


@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心界面：{}'.format(user_id)


@app.route('/<any(blog, user):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情：{}'.format(id)
    else:
        return '用户详情：{}'.format(id)


@app.route('/d/')
def d():
    wd = request.args.get('wd')
    ie = request.args.get('ie')
    print('ie:', ie)
    return '您同查询字符串的方式传递的参数是：{}'.format(wd)


if __name__ == '__main__':
    app.run(debug=True)
