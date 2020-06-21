from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def wraper(f):
    #装饰器，通用方法包装，类似拦截器
    #可考虑使用class
    def inner(req,*args,**kwargs):
        is_login=req.COOKIES.get('is_login')
        if is_login=='True':
            ret=f(req,*args,**kwargs)
        else:
            return redirect('login')
        return ret
    return inner
def index(req):

    # ret=HttpResponse('ok')
    # ret.set_cookie('k1',1)
    #header里面会带set-cookie，设置客户端cookie，之后请求会携带（同域）
    req.session['is_login']=True
    req.session['user_name']='lin'
    #1、生成session_id；随机字符串asf
    #2、在cookie里添加一个键值对 session_id:asf
    #3、将用户数据加密，保存到django-session表里，
    # return ret
    return HttpResponse('ok')

def home(req):
    print(type(req.session))
    print(req.session['is_login'])
    print(req.session['user_name'])
    #1、从cookie里取出session_id
    #2、去django里拿出数据
    #3、解密用户数据，获取用户数据
    is_login=req.COOKIES.get('k1')
    if is_login=='1':
        return render(req,'home.html')
    else:
        return HttpResponse('get out')


def func2(req):

    return HttpResponse('ok')


