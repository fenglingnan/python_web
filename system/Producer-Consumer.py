#生产者消费者通过阻塞队列/双向阻塞来进行，get和put，task_done和join
import time,random
import queue ,threading

q=queue.Queue()
def producer(name):
    count=0
    while count<10:
        print('working...')
        time.sleep(random.randrange(3))
        q.put(count)
        print('pro %s has creat %s baozi..'%(name,count))
        count+=1
        q.task_done()
        # q.join()
        print('ok')
def consumer(name):
    count=0;
    while count<10:
        time.sleep(random.randrange(4))
        if not q.empty():
            data=q.get()
            # q.task_done()
            q.join()
            # print(data)
            print('\033[32;1mconsumer %s has eat %s baozi...\033[0m'%(name,count))
        else:
            print('no baozi')#消费者速度够快或者线程够多就会产生不够
        count+=1
p1=threading.Thread(target=producer,args='A')
c1=threading.Thread(target=consumer,args='B')
c2=threading.Thread(target=consumer,args='C')
c3=threading.Thread(target=consumer,args='D')
p1.start()
c1.start()
c2.start()
c3.start()