def foo(n):
    print(n)
def bar(name):
    print('my name is %s' % name)
foo(bar)
foo(bar('lin'))
def test():
    print(1)
    return test
test()()
#map简单实现
def add_one(x):
    return x+1
def map_test(func,array):
    res=[]
    for i in array:
        res.append(func(i))
    return res
print(map_test(add_one,range(1,10)))
print(map_test(lambda x:x**3,range(0,10)))
print(list(map(lambda x:x**3,range(0,10))))
move_l=['wo','shi','tian','cai']
def filter_test(char,array):
    ret=[]
    for p in array:
        if char not in p:
            ret.append(p)
    return ret
print(filter_test('s',move_l))
#filter简单实现
def filter_test(func,array):
    ret=[]
    for p in array:
        if not func(p):
            ret.append(p)
    return ret
print(filter_test(lambda x:'s' in x,move_l))
print(list(filter(lambda x:'s' not in x,move_l)))
#reduce
from functools import reduce #python3里需导入，2不需要
int_l=[1,2,3,4,5,7,70]
def too(x,y):
    return x*y
def reduce_l(func,array):
    res = 0;
    for i in array:
        res += func(i);
    return res
# print(reduce_l(too,int_l))
print(reduce(lambda x,y:x-y,range(0,10),2))
#json形式的filter过滤
people=[
    {'name':'alex1','age':1000},
    {'name':'alex2','age':4000},
    {'name':'alex3','age':3000},
    {'name':'ax','age':18},
]
print(list(filter(lambda x:x['age']<1000,people)))