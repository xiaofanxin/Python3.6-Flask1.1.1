#url与视图函数的映射

### 传递参数：
传递参数的语法： `/<参数名>/`, 让后在视图函数中，也要定义同名的参数。

### 参数的数据类型：
1. 如果没有指定具体的参数类型,那么默认就是使用 `String` 数据类型。  
2. `int`数据类型的只能传递`int`类型。  
3. `float`数据类型只能传递`float`类型。  
4. `path`数据类型和`String`类型有点相似, 都是可以接受任意字符,但是`path`可以接受路径，也可以包含斜杠。  
5. `uuid`数据类型只能接受符合`uuid`格式的字符串, `uuid`是唯一的,可以用来做表的主键。  
6. `any`数据类型可以在一个`url`中指定多个路径,例如：  
```python
    @app.route('/<any(blog, user):url_path>/<id>/')
    def detail(url_path, id):
        if url_path == 'blog':
            return '博客详情：{}'.format(id)
        else:
            return '用户详情：{}'.format(id)           
```

### 接受用户传递的参数：  
1. 第一种：使用path的形式(将参数嵌入到路径中),就是第六点.  
2. 第二种：使用查询字符串的方式, 就是通过 `?key=value`的形式传递的.
```python
   @app.route('/d/')
    def d():
        wd = request.args.get('wd')
        return '您同查询字符串的方式传递的参数是：{}'.format(wd)
```  
3. 如果你的这个页面想要做 `SEO`优化, 就是被搜索引擎到,那么推荐使用第一种形式(path形式),如果不想在乎搜索引擎优化, 那么可以使用第二种(查询字符串的形式) 












