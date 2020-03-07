from wsgiref.simple_server import make_server
import time

def foo(url):
    f=open(url,'rb');
    data=f.read();
    return data
def show_time(req):
    times=time.ctime()
    f=open('./show_time.html','rb');
    data=f.read()
    data=data.decode('utf8')
    data=data.replace('@time@',str(times))
    return data.encode('utf8')
def router():
    url_patterns=[
        ('/login',login),
        ('/signup',signup),
        ('/show_time',show_time)
    ]
    return url_patterns
def application(environ, start_response):

    print(environ['PATH_INFO'])
    path=environ['PATH_INFO'];
    start_response('200 OK', [('Content-Type', 'text/html')])
    func=None;
    for item in router():
        if item[0]==path:
            func=item[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b'404']
def login(req):
    print(req['QUERY_STRING'])
    return b'welcome'
def signup():
    pass

port=8080

httpd = make_server('', port, application)

print('Serving HTTP on port %s...'%port)
# 开始监听HTTP请求:
httpd.serve_forever()