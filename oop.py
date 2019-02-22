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

class Room(object):
    tag=1
    def __init__(self,width,length):
        self.width=width
        self.length=length
        print(self)

    @property#把函数属性变成数据属性
    def calc_area(self):
        print("面积是%s"%(self.width*self.length))
    @classmethod#类的方法,操作类的时候用到
    def cla_mth(cls):#cls是类本身,self表示实例本身
        print(cls.tag)
    @staticmethod#静态方法,和类实例都没关系，不加@staticmethod,实例没办法调用(self问题)
    def sta_set():
        print(Room.tag+1)
r1=Room(100,100)
r1.calc_area
print(type(r1.calc_area))
Room.cla_mth()

r2=Room(5,5)
Room.sta_set()
"""
    实例只有数据属性，没有函数属性
"""
print('-'*30)
class Hand(object):
    pass
class Foot(object):
    pass
class Trunk(object):
    pass
class Head(object):
    pass
class Person(object):
    def __init__(self,id_num,name):
        self.id_num=id_num
        self.name=name
        self.hand=Hand()
        self.foot=Foot()
        self.trunk=Trunk()
        self.head=Head()

