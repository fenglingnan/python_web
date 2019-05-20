import pickle
import hashlib
import time
def create_md5():
    m = hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()

class Base(object):
    def save(self,url):
        with open(url,'wb') as f:
            pickle.dump(self,f)
class School(Base):
    def __init__(self,name,addr):
        self.id=create_md5()
        self.name=name
        self.addr=addr
    def save(self):
        super().save(self.id+'.db')
class Course(Base):
    def __init__(self,name,price,period,school):
        self.id = create_md5()
        self.name=name
        self.price=price
        self.period=period
        self.school=school
# school_obj=pickle.load(open('work.db','rb'))
# print(school_obj,'-'*10,school_obj.name,school_obj.addr)
s1=School('oldboy','北京')
# s1.save()

class Hello(object):
    _str='111'
    #单下划线开头表示私有，不应该在外部使用，python不会真的阻止调用，import里不会出现
    __star='earth'
    # 双下划线python会重新命名，_类名__属性名,无法直接访问
    stu='222'

h1=Hello();
print(h1.stu)
print(Hello.stu)


class World(object):
    feture='ugly'
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def sell(self):
        print('%s正在卖房' % self.name)

    def buy_house(self):
        print('买房')

wow=World('阿祥','厦门')
print(hasattr(wow,'name'),hasattr(wow,'sell'))
print(getattr(wow,'name'),getattr(wow,'sell'))#没有属性则报错
print(getattr(wow,'name'),getattr(wow,'sell——2222','222'))
func=getattr(wow,'sell')
func()

setattr(wow,'s1',True)#同wow.s1=True
print(wow.__dict__)

delattr(wow,'s1')#同del wow.s1
print(wow.__dict__)

test=__import__('modules')#动态导入模块,会执行导入模块里的代码,私有方法和属性会起作用
test.test1()
test.__test3()
import importlib

testdo=importlib.import_module('modules')
print(testdo)

class Foo(object):
    x=1
    def __init__(self,y):
        self.y=1

    def __getattr__(self, item):
        #调用不存在的属性时会执行
        print('执行__getattr__',item,self)
    def __delattr__(self, item):
        #删除都会触发
        print('删除操作')
    def __setattr__(self, key, value):
        print('设置属性')
        # self.key=value会递归死循环
        self.__dict__[key]=value
f=Foo(2)
del f.y
f.ss
print(f.__dict__)

class Open:
    def __init__(self,file_name,mode='r',encoding='utf-8'):
        self.file=open(file_name,mode,encoding=encoding)
        self.mode=mode
        self.encoding=encoding
    def write(self,line):
        times=__import__('time')
        self.file.write('%s %s' %(times.strftime('%Y-%m-%d %X'),line))
    def __getattr__(self, item):
        # print(item,type(item),getattr(self.file,item))
        return getattr(self.file,item)
f=Open('a.txt','w')
print(f.read)
# f.read
f.write('我是rog\n')
f.write('我是GM501\n')
f.write('我是RTX2080Ti\n')