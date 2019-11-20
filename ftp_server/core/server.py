
import json
import socketserver
import configparser
from conf import settings

STATUS_CODE={
    250:'invalid cmd format,e.g:{"action":"get","file_name":"test.py","size":"344"}',
    251:'invalid cmd',
    252:'invalid auth data',
    253:'wrong username or password',
    254:'passed authenticate',
    255:'filename doesn’t provided',
    256:'file doesn’t exist on server',
    257:'ready to send file',
    258:'md5 verification',

    800:'the file exist,but not enough ,is continue',
    801:'the file exist!',
    802:'ready to receive data',

    900:'md5 valdate success'
}


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

    def send_res(self,state_code):

        res={'status_code':state_code,'status_mes':STATUS_CODE[state_code]}

        self.request.sendall(json.dumps(res).encode('utf-8'))

    def auth(self,**data):

        username=data['username']
        password=data['password']
        user=self.authenticate(username,password)
        if user:
            self.send_res(254)
        else:
            self.send_res(253)

    def pu(self,**data):
        pass

    def authenticate(self,user,pwd):

        cfg=configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)
        if user in cfg.sections():
            if cfg[user]['Password']==pwd:
                self.user=user
                print('passion is complete')
                return user