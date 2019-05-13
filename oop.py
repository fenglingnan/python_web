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
        print(cls,'2222')
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
"""
    组合类是为了直接链接类和类的关系，比实例间的关系更好
"""
class Dad(object):
    '这是爸爸类'
    money=10
    def __init__(self,name):
        print('爸爸')
        self.name=name
    def hit_son(self):
        print('%s正在打儿子'%self.name)

class Son(Dad):
    '这是儿子类'
    money = 66666
    pass
print(Son.money)
print(Dad.__dict__)
print(Son.__dict__)
s1=Son('alex')
print(s1.money,s1.name)
s1.hit_son()
print(Son.money)#先从自身找属性和方法，没有就往父级找，非覆盖
print(Dad.money)
"""
    继承一般用做基类，基础功能的封装
    python中在继承定义好之后会有MRO(继承顺序)
    深度优先和广度优先
"""
#继承顺序
class A(object):
    def test(self):
        print('A')
class B(A):
    def test(self):
        print('B')
    # pass
class C(A):
    def test(self):
        print('C')
class D(B):
    def test(self):
        print('D')
    # pass
class E(C):
    def test(self):
        print('E')
class F(D,E):
    # def test(self):
    #     print('F')
    #从左右往右循环找父类
    pass
f1=F()
f1.test()
print(F.mro())#获得MRO顺序，最后默认一个是object基类

print('-'*50)
class Vehichle(object):
    Country='China'
    def __init__(self,name,speed,load,power):
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power
    def run(self):
        print('开动啦')

class Subway(Vehichle):
    def __init__(self,name,speed,load,power,line):
        # Vehichle.__init__(self,name,speed,load,power)
        # super().__init__(name,speed,load,power)#super不用写self，不用改父类的名称(解耦)等同于super(__class__,self)
        super(Subway,self).__init__(name,speed,load,power)#同样逻辑
        self.line = line
    def show_info(self):
        print(self.name,self.line)
    def run(self):
        # Vehichle.run(self)
        super().run()
        print('%s %s线开动啦'%(self.name,self.line))
line13=Subway('北京地铁','100m/s',10000,'elec',13)
line13.show_info()
line13.run()
print(line13.__class__)


