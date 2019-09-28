# config笔记

### 使用`app.config.from_object`的方法加载配置文件
    1、导入`import config`
    2、使用`app.config.from_object(config)`
    
### 使用`app.config.from_pyfile`的方式加载配置文件
这中方式不需要`import`,直接使用`app.config.from_pyfile('config.txt')`就可以了
注意这个地方,必须要写全文件名,后缀名也不能少。  

    1、这种方式加载配置文件，不局限于只能使用`py`文件,普通的`txt`文件同样适合
    2、这种方式可以传递`silent=True`,那么这个静态文件没有找到的时候,就不会抛出异常.




