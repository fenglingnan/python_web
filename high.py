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
    yield 1
    yield 2
g=test()
print(next(g))
print(next(g))



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
