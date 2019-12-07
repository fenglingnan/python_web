# import threading,time
#
# li=[1,2,3,4,5]
#
# def pri():
#     while li:
#         a=li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)#取得同个值，所以需要try
#         except Exception as e:
#             print('----',a,e)
#
# t1=threading.Thread(target=pri,args=())
# t1.start()
# t2=threading.Thread(target=pri,args=())
# t2.start()

#线程队列,
#先进先出
import queue
# q=queue.Queue()
q=queue.Queue()#限制数据量上限，有类似数据监听的效果
q.put(12)
q.put('hello')
q.put({'name':'yuan'})
q.put(3,False)#设置false会报错，不设置会阻塞
print(q.qsize())#长度
print(q.empty())#是否为空
print(q.full())#是否装满（初始化的上限有关）
#q.task_done()完成一项工作时，向任务完成的队列发送信号
#q.join()队列为空，即接收task_done()信号，执行其他操作
while True:
    data=q.get()
    print(data)
    print('----->')

#先进后出/后进先出
# import queue
#
# q=queue.LifoQueue()
# q.put(12)
# q.put('hello')
# q.put({'name':'123'})
#
# while True:
#     data=q.get()
#     print(data)
#     print('......~')

#优先级
# import queue
#
# q=queue.PriorityQueue()
# q.put([3,12])
# q.put([2,'hello'])
# q.put([4,{'name':'123'}])
#
# while True:
#     data=q.get()
#     print(data[1])
#     print('......~')