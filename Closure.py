import time
import basic
def timer(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print('装饰器添加成功')
        return result
    return wrapper
@timer
def test(name,age=18):
    time.sleep(3)
    print('test执行完毕',name,age)
    return 15
#@timer相当于test=timer(test)
res=test('lin',22)
print(res)

a,b,c=(1,2,3)#同es6结构赋值
print(a,b,c)
l=[1,2,3,4,45,56,5,345,2345,235,1]
a,*b,c=l;
print(a,b,c)
d=2
f=1
d,f=f,d
print(d,f)


basic.foo()()

print(basic.__name__)
import sys
print(sys.path)#解释器只认识sys.path