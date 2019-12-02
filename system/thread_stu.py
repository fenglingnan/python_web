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


if __name__ =='__main__':

    # t1=threading.Thread(target=hi,args=(3,7))#创建线程对象
    # t1.start()
    #
    # t2 = threading.Thread(target=hi, args=(4, 6))  # 创建线程对象
    # t2.start()

    s1=threading.Thread(target=music);
    s1.start()

    s2 = threading.Thread(target=game);
    s2.start()

    s1.join()#join 插入主线程之中
    # s2.join()
    print('ending...')