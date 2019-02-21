class Dog(object):
    noo=2;
    def __init__(self):
        self.name=1
        print(1)
    def do(self):
        self.no=2
dog1=Dog();
print(dog1.__dict__)#查看类得属性字典self中得
print(dog1.noo)
print(dir(Dog))
print(Dog.__bases__)#继承自哪里，默认是object
print(Dog.__module__)#模块引用
p1=Dog()
print(p1.noo)#作用域起作用
country='中国'
class Chinese(object):
    country='日本'#这个变量在class里调用的话要用类名.变量名
    def __init__(self,name):
        self.name=name;
        print('dd %s'%country)
        print(Chinese.country)

p1=Chinese('alex')
class Chinese(object):
    l=['a','b']
    def __init__(self,name):
        self.name=name;
        print('dd %s'%country)

p2=Chinese('alex')
print(p2.l)
# p2.l=[1,2,3]#改的是实例里的属性，赋值
# print(p2.l)
# print(Chinese.l)
p2.l.append('c')#改的是类里面的属性
print(p2.l)
print(p2.__dict__)
print(Chinese.l)

