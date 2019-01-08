# import sys
# import time
# print(sys.version)
# s=set('hello')
# print(s)
# s=set(['alex','alex','hello'])
# print(s)
# s={1,2,3,4,5,6}
# s.add('s')
# print(s)
# s.add(3)
# print(s)
# s.remove(2)
# s.discard(2)##删除元素不会报错
# print(s)
# p_s={'12','13','14'}
# l_s={'121','131','15'}
# d_s={'11','12'}
# print(p_s&l_s&d_s)#交集
# print(p_s|l_s|d_s)#并集
# print('差集',l_s-p_s)#被减数减去公共部分
# print(p_s^l_s)#交叉补集
# s1={1,2}
# s2={1,2,3}
# s1.update(s2)#更新多个值
# print(s1)
# d=frozenset('hello')#tuple版的set
# print(d)
# list1=['alex','alex','yqy']
# list1=list(set(list1))#去重(不考虑顺序)
# print(list1)
# """
#     99乘法表
# """
# for i in range(1,10):
#     for v in range(1,i+1):
#         print('%s * %s = %s\t'%(i,v,i*v),end='')
#     print('\t')
# """
#     公鸡5文钱1只，母鸡3文钱1只，小鸡3只一文钱，100文钱买100只鸡，公鸡母鸡小鸡都要有，各多少只？
# """
# for x in range(1,100//5):
#     for y in range(1,100//3):
#         for z in range(1,100):
#             if (x+y+z==100) and (x*5+y*3+z/3==100):
#                 print(x,y,z)
# li=('alex','eric',123)
# print(id(li))
# print(id(tuple(map(lambda x1:str(x1),li))))
# user_list=[]
# for i in range(1,31):
#     user_list.append({
#         'name':'alex'+str(i),
#         'email':'alex@live.com'+str(i),
#         'pwd':'pwd'+str(i)
#     })
# print(user_list)
# # inp=int(input('请输入页码'))
# # res=user_list[(inp-1)*10:inp*10]
# # for item in res:
# #     print(item)
# tpl="i am %(name)s age %(age)d" % {'name':'alex','age':18}
# print(tpl)
# #位置参数必须在关键字参数左边
# def test(x,*args):
#     print(x)
#     print(args)
# test(1)
# test(1,1,2,3,4,5)
# def test1(x,**kwargs):
#     print(x)
#     print(kwargs)
# test1(1,y=2,z=3)
# def test2(x,*args,**kwargs):
#     print(x,args,kwargs)
# test2(1,2,3,4,45,y=-1,z='abs')
# name='lh'
# print(id(name))
# def test3():
#     global name
#     name='ljx'
#     print(id(name))
#     def ini():
#         print(111)
#     return ini
# test3()#函数调用后才会发生全局变量的改变
# i=test3()
# print(i)
# print(id(name))
# ###全局变量的变量名大写，局部小写
# #nonlocal 上一级变量类似global
# person_list=['ljx','zxf','zzm'];
# def ask_way(per):
#     print('-'*60)
#     if len(per)==0:
#         return '根本没人知道'
#     person=per.pop(0)
#     if person=='zxf':
#         return '%s知道'% person
#     time.sleep(3)
#     return ask_way(per)
# print(ask_way(person_list))
# def test4():
#     print('in the test4')
# def test5():
#     print('in the test5')
#     return test4
# vi=test5()
# print(vi())
def foo():
    name='ljx'
    def bar():
        print(name)
    return bar
foo()()
func=lambda x:x+2
print(func(10))
#内置函数
print(abs(-1))
print(all([1,2,'-1',0]))#判断所有项bool（and）
print(all([0,False,1]))
print(bin(3))#转换2进制
print(bool(2))#bool值转换
print(bytes('你好',encoding='utf-8'))#转码
print(bytes('你好',encoding='utf-8').decode('utf-8'))#解码
print(bytes('你好',encoding='gbk'))
print(bytes('你好',encoding='gbk').decode('gbk'))
print(chr(97))#ascii表
print(ord('a'))#ascii表（和chr互逆）
print(dir(chr))#查看内置方法__init__之类
print(divmod(10,3))#取余数，商（分页用）
print(eval('[1,2,3]'))#提取字符串,运行里面的内容
print(hash((12,3,4)))#只有不可变类型才可哈希
print(list(zip(('a','b','c','d'),(1,2,3))))#拉链效果,非一一对应就删除
p={'name':'alex','age':18}
print(list(zip(p.keys(),p.values())))
l=[1,2,5,7,-2,100]
print(max(l))
print(min(l))
people=[
    {'name':'alex1','age':1000},
    {'name':'alex2','age':4000},
    {'name':'alex3','age':3000},
    {'name':'ax','age':18},
]
#max里传的是dict默认比较是dict的key
print(max(people,key=lambda x:x['age']))
print(pow(2,3))#幂次运算
print(pow(2,3,2))#2**3%2
print(list(reversed(l)))#反转，不保存结果，不影响原数据
print(set('hello'))#去重变为元组
print(sorted(l))#排序
print(sorted(people,key=lambda x:x['age'],reverse=True))
def testn():
    name='v啊狂顶v拿到v你'
    print(locals())
    print(vars())
testn()
print(vars(int))

#两种import,__import__引入字符串类型
# import Advanced
# Advanced.foo('d')
module_name='Advanced'
m=__import__(module_name)
m.foo('sb')