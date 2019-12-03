

import threading,time
def add():
    sum=0
    digital=0
    while digital<=1000000:
        sum += digital
        digital+=1
    print(sum)

def multiply():
    multiply=1
    digital=1
    while digital<=20000:
        multiply *= digital
        digital+=1
    print(multiply)
# print(add())
# print(multiply())
start=time.time()
math1=threading.Thread(target=add)
math2=threading.Thread(target=multiply)

l=[]
l.append(math1)
l.append(math2)
# for t in l:
#     t.start()
# for t in l:
#     t.join()
#gil阻止多线程，同一时刻只有一个线程
#用多进程+协程解决
#任务分为IO密集型和计算密集型，python多线程，多进程+协程，对于IO密集型有意义，对于计算密集型可能会有反作用
add()
multiply()
print('cost time %s'%(time.time()-start))