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
s1.save()