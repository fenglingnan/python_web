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

    ret=HttpResponse('ok')
    ret.set_cookie('k1',1)
    return ret

def home(req):
    print(req.COOKIES)
    is_login=req.COOKIES.get('k1')
    if is_login=='1':
        return render(req,'home.html')
    else:
        return HttpResponse('get out')