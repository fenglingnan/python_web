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