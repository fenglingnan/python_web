import time
"""
    三元表达式
"""
name='alex'
res='sb_alex' if name=='alex' else '帅哥'
print(res)
#列表解析
egg_list=['鸡蛋%s' %i for i in range(10)]
egg_list1=['鸡蛋%s' %i for i in range(10) if i>5]#三元，无四元
print(egg_list)
print(egg_list1)
chick=('鸡蛋%s' %i for i in range(10))#生成器表达式，[]换成()
print(chick)
print(chick.__next__())
# print(sum(i for i in range(10000000)))


l=[1,2,3]
for i in l:
    print(i)
#for 循环调用__iter__方法
l_next=l.__iter__()
print(l_next)
print(l_next.__next__())
# print(l_next.__next__())
# print(l_next.__next__())
print(next(l_next))#内置函数，取迭代器的值
def test():
    yield 111
    print('这是第一次之后')
    yield 222
    yield 333
g=test()
print(next(g))
print(next(g))
print(next(g))

def product():
    for i in range(100):
        yield '一屉包子%s' %i
bz=product()
print(next(bz))
print(next(bz))
#生成器只能遍历一次，遍历完成后在内存中删除

# def consumer(name):
#     print('我是[%s],我准备开始吃包子了'%name);
#     while True:
#         baozi=yield
#         time.sleep(1)
#         print('%s 很开心的把[%s]吃掉了'%(name,baozi))
# def producter():
#     c1=consumer('阿祥');
#     c1.__next__();
#     for i in range(10):
#         time.sleep(1)
#         c1.send('猪肉粉丝馅%s' %i)
# producter()

def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs);
        stop_time=time.time()
        print('函数运行时间是%s'%(stop_time-start_time))
        return res
    return wrapper
@timer
def cal(l):
    res=0;
    for i in l:
        time.sleep(0.1)
        res+=i
    return res

cal(range(20))
# print(cal(range(20)))