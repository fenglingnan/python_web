# from multiprocessing import Process
# import time
# def f(name):
#     time.sleep(1)
#     print('hello', name,time.ctime())
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = Process(target=f, args=('alvin',))
#         p_list.append(p)
#         p.start()
#     for i in p_list:
#         p.join()
#     print('end')
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()
#         #self.name = name
#
#
#     def run(self):
#         time.sleep(1)
#         # self.name是进程的名字
#         print ('hello', self.name,time.ctime())
#
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = MyProcess()
#         p.daemon=True
#         p.start()
#         p_list.append(p)
# print('end')
# from multiprocessing import Process
# import os
# import time
#
# #pid：process id
# def info(title):
#     print("title:", title)
#     print('parent process:', os.getppid())#父进程pid
#     print('process id:', os.getpid())#进程pid
#
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     info('main process line')
#     time.sleep(1)
#     print("------------------")
#     p = Process(target=info, args=('yuan',))
#     p.start()
#     p.join()
# import multiprocessing
# import queue
#
# def foo(q):
#     q.put(123)
#     q.put(456)
#
# if __name__ == '__main__':
#
#     # q=queue.Queue()#线程队列
#     q=multiprocessing.Queue()#进程队列
#     p=multiprocessing.Process(target=foo,args=(q,))
#
#     p.start()
#
#     print(q.get())
#     print(q.get())

# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([12, {"name":"yuan"}, 'hello'])
#     response=conn.recv()
#     print("response",response)
#     conn.close()
#     print("q_ID2:",id(conn))
#
# if __name__ == '__main__':
#
#     parent_conn, child_conn = Pipe()#双向管道
#     print("q_ID1:",id(child_conn))
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     parent_conn.send("儿子你好!")
#     p.join()

from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    # d[0.25] = None
    l.append(n)
    #print(l)

    print("son process:",id(d),id(l))

if __name__ == '__main__':

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))

        print("main process:",id(d),id(l))

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d,l,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)