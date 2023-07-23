#!/usr/bin/python3
# coding:utf-8
import os
from wsgiref.simple_server import make_server

import pkg_resources


def app(env, make_response):
    # 处理业务最核心的函数

    '''
    请求路径：PATH_INFO，以 / 开头
    请求方法：REQUEST_METHOD
    请求查询参数：QUERY_STRING
    客户端地址：HTTP_REFERER
    客户端的地址：REMOTE_ADDR
    请求上传数据的类型：CONTENT_TYPE
    客户端的代理（浏览器）：HTTP_USER_AGENT
    读取请求上传的字节数据对象：wsgi.input
    wsgi是否使用了多线程：wsgi.multithread
    wsgi是否使用了多进程：wsgi.multiprocess
    '''
    # for k, v in env.items():
    #     print(k, ':', v)

    path = env.get('PATH_INFO')  # 获取请求资源的路径
    headers = []  # 响应头，根据响应的数据增加不同的响应头 k:v
    body = []  # 响应的数据

    # 设置静态资源的目录
    static_dir = 'html'
    if path == '/favicon.ico':
        res_path = os.path.join(static_dir, 'image/BjPyLGPNp3.jpg')
        headers.append(('content-type', 'image/*'))
    elif path == '/':
        # 主页
        res_path = os.path.join(static_dir, 'example_of_jquery_3.html')
        headers.append(('content-type', 'text/html;charset=utf-8'))
    else:
    # 其他资源：css/js/图片/MP4/MP3
        res_path = os.path.join(static_dir,path[1:])
        if res_path.endswith('.html'):
            headers.append(('content-type', 'text/html;charset=utf-8'))
        elif any((res_path.endswith('.png'),
                 res_path.endswith('.jpg'),
                 res_path.endswith('.gif'))):
            headers.append(('content-type', 'image/*'))
        else:
            headers.append(('content-type', 'text/*;charset=utf-8'))

    # 生成响应的头
    # make_response('200 OK',
    #              [('Content-Type', 'text/html;charset=utf-8')])
    # return ['<h3>Hi,WSGI</H3>'.encode('utf-8')]  # 响应数据

    # 判断资源是否存在 res_path
    status_code = 200
    if not os.path.exists(res_path):
        status_code = 404
        body.append('<h4 style="color:red">请求的资源不存在：404</h4>'.encode('utf-8'))
    else:
        with open(res_path,'rb') as f:
            body.append(f.read())

    make_response('%s OK' % status_code,headers)
    return body



# 生成web应用服务进程
host = '0.0.0.0'
port = 8000
httpd = make_server(host, port, app)
print('running http://%s:%s' % (host, port))

# 启动服务，开始监听客户端连接
httpd.serve_forever()
