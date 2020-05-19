from django.shortcuts import render,HttpResponse,redirect
import time

#views里面加函数默认值处理多种情况

# Create your views here.
#用装饰器给函数做拦截
#继承dispatch给class做拦截


def dec(func):
    def run(*args,**kwargs):
        print('请求之前')
        ret=func(*args,**kwargs)
        print('请求之后')
        return ret
    return run


@dec
def show_time(req):

    name_list=[
        'lin',
        'huang',
        'hu'
    ]
    # return HttpResponse('hello')
    t=time.ctime()
    b=2
    return render(req,'index.html',locals())

def articles_year(req,year):

    return HttpResponse(year)

def articles_year_mon(req,year,month):
    print(year,month)
    return HttpResponse(year+month)

def register(req):
    print(req.method)
    print(req.path)
    print(req.get_full_path())
    user=req.POST.get('user')
    if req.method=='POST':
        # print(req.GET)
        print(req.POST,77777)
        if user=='lin':
            return redirect('/login')
            # return render(req,'login.html')用render跳转，url不变
        return HttpResponse('success!')
    return render(req,'register.html')

def login(req):
    return render(req,'login.html')

def notfound(req,exception,template_name='404.html'):
    return render(req,template_name)

def index(req):
    print(req.method,req.GET)
    t = time.ctime()
    return render(req,'index.html',{'t':t})
def all_url(req):
    return render(req,'red.html')

def blog404(req):
    return render(req,'blog404.html')


from django.views import View
from django.utils.decorators import method_decorator
class LoginView(View):

    def dispatch(self, request, *args, **kwargs):

        ret=super().dispatch(request, *args, **kwargs);
        #请求前的拦截，重写dispatch
        #请求前都过的方法，分发
        return ret

    @method_decorator(dec)#类的装饰器参考方法的装饰器
    def get(self,request):

        return render(request,'login2.html')

    def post(self,request):
        username=request.POST.get('username')
        userpwd = request.POST.get('userpwd')

        print(username,userpwd)
        return HttpResponse('hello world')

def feng(req):
    if req.method=='GET':
        return render(req,'feng.html')
    if req.method=='POST':
        return HttpResponse('成功')

def base(req):
    return render(req,'base.html')

def get_base(req):
    return render(req,'get_base.html')

def diy(req):

    s1='miya'
    l1=[11,23,3,54,5]
    return render(req,'tags.html',{'s1':s1,'l1':l1})