from django.shortcuts import render

# Create your views here.

def login(req):
    if req.method=='GET':
        return render(req,'login.html')
    if req.method=='GET':
        pass

def register(req):

    if req.method=='GET':
        return render(req,'register.html')