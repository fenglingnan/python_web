# import threading #线程
# import time
# def hi(num,load):
#     print(num,load)
#     #time.sleep(1)#多线程同时异步
#
# def music():
#     print('start',time.ctime())
#     time.sleep(2)
#     print('end',time.ctime())
#
# def game():
#     print('play',time.ctime())
#     time.sleep(2)
#     print('play_end',time.ctime())
#
#
# if __name__ =='__main__':
#
#     # t1=threading.Thread(target=hi,args=(3,7))#创建线程对象
#     # t1.start()
#     #
#     # t2 = threading.Thread(target=hi, args=(4, 6))  # 创建线程对象
#     # t2.start()
#
#     s1=threading.Thread(target=music);
#     s1.start()
#
#     s2 = threading.Thread(target=game);
#     s2.start()
#
#     s1.join()#join 插入主线程之中
#     # s2.join()
#     print('ending...')
import threading #线程
import time
def hi(num,load):
    print(num,load)
    #time.sleep(1)#多线程同时异步

def music():
    print('start',time.ctime())
    time.sleep(2)
    print('end',time.ctime())

def game():
    print('play',time.ctime())
    time.sleep(2)
    print('play_end',time.ctime())

thred=[]
t1=threading.Thread(target=music)
t2=threading.Thread(target=game)
thred.append(t1)
thred.append(t2)

if __name__ =='__main__':
    # t2.setDaemon(True)
    for t in thred:

        t.start()
        print('count:%d'%threading.active_count())

    # t1.join()
    #t1.setDaemon(True)
    '''setDaemon必须在start之前,守护进程,主线程结束就放弃执行分支线程'''

    print('over','-'*50)

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数
                    # run是重写父类的方法，用其他名字不行

        print("running on number:%s" % self.num)

        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

    print("ending......")



#并发是轮流处理多个任务，并行是同时处理多个任务