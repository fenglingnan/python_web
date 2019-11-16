import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        #必须重新定义一个handle方法
        print(self.request) #conn
        print(self.client_address) #addr

        while True:
            try:
                #收消息
                data=self.request.recv(1024);
                if not data:
                    break
                print('收到客户端消息是',data)

                #发消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    #通过不同实例来执行多线程，实现并发（简易版并发）
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),Myserver)
    s.serve_forever()