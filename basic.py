import sys
print(sys.version)
s=set('hello')
print(s)
s=set(['alex','alex','hello'])
print(s)
s={1,2,3,4,5,6}
s.add('s')
print(s)
s.add(3)
print(s)
s.remove(2)
s.discard(2)##删除元素不会报错
print(s)
p_s={'12','13','14'}
l_s={'121','131','15'}
d_s={'11','12'}
print(p_s&l_s&d_s)#交集
print(p_s|l_s|d_s)#并集
print('差集',l_s-p_s)#被减数减去公共部分
print(p_s^l_s)#交叉补集
s1={1,2}
s2={1,2,3}
s1.update(s2)#更新多个值
print(s1)
d=frozenset('hello')#tuple版的set
print(d)
list1=['alex','alex','yqy']
list1=list(set(list1))#去重(不考虑顺序)
print(list1)
"""
    99乘法表
"""
for i in range(1,10):
    for v in range(1,i+1):
        print('%s * %s = %s\t'%(i,v,i*v),end='')
    print('\t')
"""
    公鸡5文钱1只，母鸡3文钱1只，小鸡3只一文钱，100文钱买100只鸡，公鸡母鸡小鸡都要有，各多少只？
"""
for x in range(1,100//5):
    for y in range(1,100//3):
        for z in range(1,100):
            if (x+y+z==100) and (x*5+y*3+z/3==100):
                print(x,y,z)
li=('alex','eric',123)
print(id(li))
print(id(tuple(map(lambda x1:str(x1),li))))
user_list=[]
for i in range(1,31):
    user_list.append({
        'name':'alex'+str(i),
        'email':'alex@live.com'+str(i),
        'pwd':'pwd'+str(i)
    })
print(user_list)
# inp=int(input('请输入页码'))
# res=user_list[(inp-1)*10:inp*10]
# for item in res:
#     print(item)
tpl="i am %(name)s age %(age)d" % {'name':'alex','age':18}
print(tpl)
#位置参数必须在关键字参数左边
def test(x,*args):
    print(x)
    print(args)
test(1)
test(1,1,2,3,4,5)
def test1(x,**kwargs):
    print(x)
    print(kwargs)
test1(1,y=2,z=3)
def test2(x,*args,**kwargs):
    print(x,args,kwargs)
test2(1,2,3,4,45,y=-1,z='abs')