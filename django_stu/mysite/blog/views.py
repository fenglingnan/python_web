from django.shortcuts import render,HttpResponse
import time

# Create your views here.
def show_time(req):


    # return HttpResponse('hello')
    t=time.ctime()
    return render(req,'index.html',{'t':t})

def articles_year(req,year):

    return HttpResponse(year)

def articles_year_mon(req,year,month):

    return HttpResponse(year+month)

def register(req):
    print(req.method,66666)
    if req.method=='POST':
        # print(req.GET)
        print(req.POST,77777)
        return HttpResponse('success!')
    return render(req,'register.html')