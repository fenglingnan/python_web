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