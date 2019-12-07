import threading,time
#->表示类型提示（返回值）
#同个event事件控制多线程的处理，类似于多线程锁
class Boss(threading.Thread):

    def run(self):
        print('boss:今晚加班')
        print(event.isSet())
        event.set()
        time.sleep(5)
        print('boss:下班了')
        print(event.isSet())#返回false是因为下方有clear，clear重置为false
        event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait()#event.isSet=true通过
        print('难受')
        time.sleep(1)
        event.clear()
        event.wait()
        print('yeah')

if __name__ =='__main__':
    event=threading.Event()

    th=[]
    for i in range(5):
        th.append(Worker())
    th.append(Boss())
    for i in th:
        i.start()
    for i in th:
        i.join()
