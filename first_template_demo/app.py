from flask import Flask, render_template

app = Flask(__name__)
# 可以在实例时指定模板文件的位置(修改默认模板文件位置)，设置其template_folder参数，值为路径。


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/list/')
def my_list():
    return render_template('posts/list.html')


if __name__ == '__main__':
    app.run()
