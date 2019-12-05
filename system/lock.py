# import threading
# import time
# def sub():
#
#     global num
#     lock.acquire()#同步锁
#     temp=num
#     time.sleep(0.1)
#     num=temp-1
#     lock.release()#释放同步锁
#
# num=100
# l=[]
# lock=threading.Lock()
# for i in range(100):
#     t=threading.Thread(target=sub)
#     t.start()
#     l.append(t)
#
# for i in l:
#     t.join()
#
# print(num)



'''递归锁
    线程需要互相的release释放，造成死锁
'''
import threading,time

class myThread(threading.Thread):
    def doA(self):
        r_lock.acquire()
        print(self.name,"gotlockA",time.ctime())
        time.sleep(3)
        r_lock.acquire()
        print(self.name,"gotlockB",time.ctime())
        r_lock.release()
        r_lock.release()

    def doB(self):
        r_lock.acquire()
        print(self.name,"gotlockB",time.ctime())
        time.sleep(2)
        r_lock.acquire()
        print(self.name,"gotlockA",time.ctime())
        r_lock.release()
        r_lock.release()

    def run(self):
        self.doA()
        self.doB()
if __name__=="__main__":

    # lockA=threading.Lock()
    # lockB=threading.Lock()
    r_lock=threading.RLock()#内部有个count，等于0的时候才会执行同步锁,release的时候-1
    threads=[]
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()#等待线程结束，后面再讲。

