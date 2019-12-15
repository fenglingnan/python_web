import threading,time

class msignal(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()


if __name__ =='__main__':
    semaphore=threading.Semaphore(5)
    #控制并发数总量
    th=[]
    for i in range(100):
        th.append(msignal())
    for i in th:
        i.start()
    # for i in th:
    #     i.join()