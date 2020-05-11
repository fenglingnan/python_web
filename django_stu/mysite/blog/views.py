from django.shortcuts import render,HttpResponse,redirect
import time

#views里面加函数默认值处理多种情况

# Create your views here.
def show_time(req):


    # return HttpResponse('hello')
    t=time.ctime()
    return render(req,'index.html',{'t':t})

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