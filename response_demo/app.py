from flask import Flask, Response, jsonify

app = Flask(__name__)


class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """
        这个方法只有视图函数返回非字符、非元组、非Response对象
        :param response: 视图函数的返回值
        :param environ:
        :return:
        """
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)


app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return Response('Hello World!', status=200, content_type='text/html')
    # return 'Hello World!'


@app.route('/list1/')
def list1():
    return Response('Fanxin')


@app.route('/list2/')
def list2():
    return 'list2', 200, {'X-NAME': 'FANXIN'}


@app.route('/list3/')
def list3():
    return {'username': 'fanxin', 'password': '123456'}


if __name__ == '__main__':
    app.run()
