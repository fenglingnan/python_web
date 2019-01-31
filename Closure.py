import time
# import basic
import random,sys
# def timer(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         print('装饰器添加成功')
#         return result
#     return wrapper
# @timer
# def test(name,age=18):
#     time.sleep(3)
#     print('test执行完毕',name,age)
#     return 15
# #@timer相当于test=timer(test)
# res=test('lin',22)
# print(res)
#
# a,b,c=(1,2,3)#同es6结构赋值
# print(a,b,c)
# l=[1,2,3,4,45,56,5,345,2345,235,1]
# a,*b,c=l;
# print(a,b,c)
# d=2
# f=1
# d,f=f,d
# print(d,f)
#
#
# basic.foo()()
#
# print(basic.__name__)
# import sys
# print(sys.path)#解释器只认识sys.path
# print(sys.platform)
# print(time.time())#生成的时间戳是秒数
# print(time.localtime())
# print(time.localtime().tm_year)
# print(time.gmtime())#格林尼治时间utc，世界标准时间
# print(time.mktime(time.localtime()))
# print(time.strftime("%Y-%m-%d %X",time.localtime()))
# print(time.strftime("%Y-%m-%d %H-%M-%S %Z",time.localtime()))
# print(time.strptime("2019:1:20 22:48:22","%Y:%m:%d %X"))
# print(time.asctime())
# print(time.ctime())
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime)
# print(datetime.datetime.tzinfo)

def v_code():
    ret=''
    for i in range(6):
        num=random.randint(0,9)
        af=chr(random.randint(65,90))
        alf=chr(random.randint(97,122))
        s=str(random.choice([num,alf,af]))
        ret+=s
    return ret
print(v_code())
import os,sys
print(os.getcwd())#获得当前目录
os.chdir('..')#相当于cd
print(os.getcwd())
print(os.listdir(os.getcwd()))#打印当前目录
print(os.stat('python_web/high.py'))#获取操作文件时间（经常使用st_mtime，modify修改时间），size是用B做单位
print(os.sep)#目录分隔符
print(os.linesep)
print(sys.platform)
a='G:\git'
b='python_web\high.py'
# print(os.path.join(a,b))#合并路径
# print(os.path.getmtime(os.path.join(a,b)))
print(os.environ)#系统环境变量
print(sys.argv,sys.version)