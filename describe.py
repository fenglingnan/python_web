# def test(x):
#     print(type(x)==dict)
#     print('===>',x)
#
# test({'a':2})
class Type:
    def __init__(self,key,types):
        self.key=key
        self.types=types
    def __get__(self, instance, owner):
        print('get方法')
        print('instance %s owner %s'%(instance,owner))
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('set方法')
        # print('instance:%s,value:%s'%(instance,value))#instance就是实例
        if not isinstance(value,self.types):
            print('传入的值不是%s'%str(self.types).split('\'')[-2])
            return
            # raise TypeError('传入的值不是字符串类型')
        instance.__dict__[self.key]=value

def p_deco(**kwargs):
    def wrapper(obj):
        for key,val in kwargs.items():
            setattr(obj,key,Type(key,val))
        return obj
    return wrapper

@p_deco(name=str,age=int,salary=dict)
class People:
    # name=Type('name',str)
    # age=Type('age',int)
    # salary=Type('salary',dict)
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('xiang',18.2,30.2)
# p1.name
# p1.name=333
# p1.age='333'
print('---->',p1.__dict__)

def Typed(**kwargs):
    def deco(obj):
        # obj.__dict__=dict(obj.__dict__,**kwargs)#不能混合，obj.__dict__不可写
        for key,val in kwargs.items():
            setattr(obj,key,val)
        return obj
    return deco

@Typed(x=1,y=2,z=3)   #Foo=deco(Foo)
class Foo:
    pass

print(Foo.__dict__)