# def foo(n):
#     print(n)
# def bar(name):
#     print('my name is %s' % name)
# foo(bar)
# foo(bar('lin'))
# def test():
#     print(1)
#     return test
# test()()
# #map简单实现
# def add_one(x):
#     return x+1
# def map_test(func,array):
#     res=[]
#     for i in array:
#         res.append(func(i))
#     return res
# print(map_test(add_one,range(1,10)))
# print(map_test(lambda x:x**3,range(0,10)))
# print(list(map(lambda x:x**3,range(0,10))))
# move_l=['wo','shi','tian','cai']
# def filter_test(char,array):
#     ret=[]
#     for p in array:
#         if char not in p:
#             ret.append(p)
#     return ret
# print(filter_test('s',move_l))
# #filter简单实现
# def filter_test(func,array):
#     ret=[]
#     for p in array:
#         if not func(p):
#             ret.append(p)
#     return ret
# print(filter_test(lambda x:'s' in x,move_l))
# print(list(filter(lambda x:'s' not in x,move_l)))
# #reduce
# from functools import reduce #python3里需导入，2不需要
# int_l=[1,2,3,4,5,7,70]
# def too(x,y):
#     return x*y
# def reduce_l(func,array):
#     res = 0;
#     for i in array:
#         res += func(i);
#     return res
# # print(reduce_l(too,int_l))
# print(reduce(lambda x,y:x-y,range(0,10),2))
# #json形式的filter过滤
# people=[
#     {'name':'alex1','age':1000},
#     {'name':'alex2','age':4000},
#     {'name':'alex3','age':3000},
#     {'name':'ax','age':18},
# ]
# print(list(filter(lambda x:x['age']<1000,people)))
l=open('open.txt',encoding='utf-8')
# data=l.read()
# print(data)
print(l.readlines())

l.close()
s=open('open.txt','w',encoding='utf-8')
s.write('2222\n')
s.write('22222223\n')
s.writelines(['33333\n','444444\n'])
#s.writelines(['33333\n','444444\n',1])#不可写其他类型，只能写str
s.close()

add=open('open.txt','a',encoding='utf-8')
add.write('ddddddd\n')
add.writelines(['1313413431\n','asdvadva'])
add.close()

src_f=open('open.txt','r',encoding='utf-8')
data=src_f.readlines()
src_f.close()

dst_f=open('open_new.txt','w',encoding='utf-8')
#dst_f.writelines(data)
print(data)
dst_f.writelines(data[0:-1:2])
dst_f.close()

with open('open_new.txt','w',encoding='utf-8') as f:
    f.write('我是with生成\n')
    f.write('我是with生成')
with open('open_new.txt','r',encoding='utf-8') as f,\
    open('open.txt','w',encoding='utf-8') as g:
    data=f.readlines()
    g.writelines(data)
#b模式只有2进制编码,不能指定编码
ddd=open('open.txt','rb')
ss=ddd.read()
print(ss.decode('utf-8'))
ddd.close()
eee=open('open.txt','wb')
print(bytes('自促\n',encoding='utf-8'))
eee.write(bytes('自促\n',encoding='utf-8'))
eee.write('祥'.encode('utf-8'))
print(eee.tell())#光标位置
eee.seek(0)#光标移动到某个位置
print(eee.tell())
#eee.truncate()文件截取