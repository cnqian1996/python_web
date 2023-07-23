from flask import Flask

# 创建Flask对象-Httpd WEB服务对象
app = Flask('hiflask')  # __name__可以是任意的小写字母，表示Flask应用对象名称


# 声明WEB服务的请求资源（指定资源访问的路由）
@app.route('/hi', methods=['GET', 'POST'])
def hi():
    # 使用request请求对象，获取请求方法
    from flask import request
    if request.method == 'GET':
        return """
        <h1>用户登录页面</h1>
        <form action="hi" method="post">
            <input name="name" placeholder="用户名"><br>
            <input name="pwd" placeholder="口令"><br>
            <button>提交</button>
        </from>
        """
    else:
        # 获取表单参数
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        if all((
                name == 'zhengyi',
                pwd == 'sb945'
        )):
            return '''
                <h2 style="color:red;">登录成功</h3>           
            '''
        else:
            return '''
                 <h2 style="color:orange;">登录失败！<a href="/hi">重试</a></h3>           
            '''

# 启动服务
app.run('localhost', 5000)
