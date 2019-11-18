
import json
import socketserver

class ServerHandler(socketserver.BaseRequestHandler):

    def handle(self):

        while True:
            #conn=self.request
            data=self.request.recv(1024).strip()
            data=json.loads(data.decode('utf-8'))
            if data.get('action'):
                if hasattr(self,data.get('action')):
                    func=getattr(self,data.get('action'))
                    func(**data)
                else:
                    print('invalid cmd')
            else:
                print('invalid cmd')
    def auth(self,**data):

        print('data is',data)

    def pu(self,**data):
        pass
