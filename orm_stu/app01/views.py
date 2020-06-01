from django.shortcuts import render
from app01 import models
from django.views import View
from django.http import HttpResponse
import json

# Create your views here.
def index(req):

    #创建数据，创建记录
    #创建方式1
    # userinfo=models.UserInfo(
    #     id=5,
    #     name='dazhuang',
    #     age=18,
    #     current_data='2017-01-02'
    # )
    # userinfo.save()
    #创建方式2
    # new_obj=models.UserInfo.objects.create(name='set',age=17,current_data='2017-03-02')
    # print(new_obj)
    #创建方式3 批量创建
    # objs=[]
    # for i in range(20):
    #     obj= models.UserInfo(
    #         age=123+i,
    #         name='6677'+str(i),
    #         current_data='2020-09-09'
    #     )
    #     objs.append(obj)
    # models.UserInfo.objects.bulk_create(objs)
    #创建方法4update_or_create有就更新，没有就创建
    # models.UserInfo.objects.update_or_create(
    #     name='6670',
    #     defaults={
    #         'age':49,
    #         'current_data':'2020-02-02'
    #     }
    # )



    #简单查询
    # all_obj=models.UserInfo.objects.all()
    # print(all_obj)#返回可迭代对象类似json格式
    # objs=models.UserInfo.objects.filter(id=5)#filter返回也是列表，就算只有一个数据也是列表包裹
    # print(objs[0].id)
    #条件查询 get必须有且仅有一条记录，否则报错，如果为空也报错
    # obj=models.UserInfo.objects.get(id=5)
    # print(obj,obj.name,type(obj))

    #delete (query对象和model对象都可以使用)
    # models.UserInfo.objects.get(id=5).delete()
    #删除所有无法直接删除，需调用all触发delete
    #models.UserInfo.objects.all().delete()
    #更新 model对象不能调用更新方法 只能queryset调用
    #models.UserInfo.objects.get(id=6).update(age=22)
    #models.UserInfo.objects.filter(id=6).update(age=22)


    #重点查询
    '''
        <1> all():                  查询所有结果，结果是queryset类型

<2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象，结果也是queryset类型 Book.objects.filter(title='linux',price=100) #里面的多个条件用逗号分开，并且这几个条件必须都成立，是and的关系，or关系的我们后面再学，直接在这里写是搞不定or的

<3> get(**kwargs):          返回与所给筛选条件相匹配的对象，不是queryset类型，是行记录对象，返回结果有且只有一个，
                            如果符合筛选条件的对象超过一个或者没有都会抛出错误。捕获异常try。  Book.objects.get(id=1)

<4> exclude(**kwargs):      排除的意思，它包含了与所给筛选条件不匹配的对象，没有不等于的操作昂，用这个exclude，返回值是queryset类型 Book.objects.exclude(id=6)，返回id不等于6的所有的对象，或者在queryset基础上调用，Book.objects.all().exclude(id=6)
 　　　　　　　　　　　　　　　　
<5> order_by(*field):       queryset类型的数据来调用，对查询结果排序,默认是按照id来升序排列的，返回值还是queryset类型
　　　　　　　　　　　　　　　　  models.Book.objects.all().order_by('price','id') #直接写price，默认是按照price升序排列，按照字段降序排列，就写个负号就行了order_by('-price'),order_by('price','id')是多条件排序，按照price进行升序，price相同的数据，按照id进行升序

<6> reverse():              queryset类型的数据来调用，对查询结果反向排序，返回值还是queryset类型

<7> count():                queryset类型的数据来调用，返回数据库中匹配查询(QuerySet)的对象数量。

<8> first():                queryset类型的数据来调用，返回第一条记录 Book.objects.all()[0] = Book.objects.all().first()，得到的都是model对象，不是queryset

<9> last():                queryset类型的数据来调用，返回最后一条记录

<10> exists():              queryset类型的数据来调用，如果QuerySet包含数据，就返回True，否则返回False
　　　　　　　　　　　　　　     空的queryset类型数据也有布尔值True和False，但是一般不用它来判断数据库里面是不是有数据，如果有大量的数据，你用它来判断，那么就需要查询出所有的数据，效率太差了，用count或者exits
　　　　　　　　　　　　　　　　 例：all_books = models.Book.objects.all().exists() #翻译成的sql是SELECT (1) AS `a` FROM `app01_book` LIMIT 1，就是通过limit 1，取一条来看看是不是有数据

<11> values(*field):        用的比较多，queryset类型的数据来调用，返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
                            model的实例化对象，而是一个可迭代的字典序列,只要是返回的queryset类型，就可以继续链式调用queryset类型的其他的查找方法，其他方法也是一样的。
<12> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列

<13> distinct():            values和values_list得到的queryset类型的数据来调用，从返回结果中剔除重复纪录


    可链式调用.filter(id=1,name='123').update()
    写法可变换 .filter(**{id:1,name:'123})
    '''



    return render(req,'index.html')

class LoginView(View):

    def get(self,req):

        return render(req,'login.html')

def test(req):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")