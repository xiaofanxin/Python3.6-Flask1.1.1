from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 一个url中，含有手机号码的变量，必须限定这个变量的字符串格式满足手机号码的格式


class TelephoneConverter(BaseConverter):
    regex = r'1[8573]\d{9}'


class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return '+'.join(value)


app.url_map.converters['tel'] = TelephoneConverter
app.url_map.converters['list'] = ListConverter


@app.route('/')
def hello_world():
    return url_for('posts', boards=['a', 'b'])


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return '您输入的用户ID:{}'.format(user_id)


@app.route('/telephone/<tel:my_telephone>/')
def my_tel(my_telephone):
    return '您的手机号码是: %s' % my_telephone


@app.route('/posts/<list:boards>/')
def posts(boards):
    return '您提交的板块是： {}'.format(boards)


if __name__ == '__main__':
    app.run()
