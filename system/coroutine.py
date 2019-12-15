'''
协程最重要的是yield，多段式返回
协程主要是为了io操作不是为了计算密集型
'''
####yield回顾
# def f():
#     print('ok')
#     s=yield 6#yield是输出值 s是generator方法输入的值
#     print(s)
#     print('ok2')
#     yield
#
# gen=f()
# print(gen)
# res=gen.__next__()
# print(res)
# gen.send(5)#generator.send


# import time
# import queue
#
# def consumer(name):
#     print("--->ready to eat baozi...")
#     while True:
#         new_baozi = yield
#         print("[%s] is eating baozi %s" % (name,new_baozi))
#         #time.sleep(1)
#
# def producer():
#
#     r = con.__next__()
#     r = con2.__next__()
#     n = 0
#     while 1:
#         time.sleep(1)
#         print("\033[32;1m[producer]\033[0m is making baozi %s and %s" %(n,n+1) )
#         con.send(n)
#         con2.send(n+1)
#
#         n +=2
#         if n>=60:
#             return
#
#
# if __name__ == '__main__':
#     con = consumer("c1")
#     con2 = consumer("c2")
#     p = producer()

# from greenlet import greenlet
#
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

import gevent

import requests,time


start=time.time()

def f(url):
    print('GET: %s' % url)
    resp =requests.get(url)
    data = resp.text
    # print(data)
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([

        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.sina.com.cn/'),

])

# f('https://www.python.org/')
# f('https://www.yahoo.com/')
# f('https://www.sina.com.cn/')
# f('http://www.baidu.com')
print("cost time:",time.time()-start)