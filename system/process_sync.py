# from multiprocessing import Process,Lock
#
# def f(l,i):
#     l.acquire()
#     print('hello %s',i)
#     l.release()
#
#
# if __name__ =="__main__":
#     lock=Lock()
#     for num in range(10):
#         Process(target=f,args=(lock,num)).start()
from  multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(1)
    print(i)
    return i+100

def Bar(arg):

    print(os.getpid())
    print(os.getppid())
    print('logger:',arg)

if __name__ == '__main__':
    pool = Pool()

    Bar(1)
    print("----------------")

    for i in range(10):
        # pool.apply(func=Foo, args=(i,))
        # pool.apply_async(func=Foo, args=(i,))
        #回调函数在父进程调用，为了打印日志
        #Foo方法return的值赋给了Bar作为参数
        pool.apply_async(func=Foo, args=(i,), callback=Bar)

    pool.close()#close必须在join上面，必须有close
    pool.join()
    print('end')