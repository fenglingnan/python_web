
import json
import socketserver
import configparser
from conf import settings
import os

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

    def put(self,**data):

        print('data',data)
        has_received=0
        file_name=data.get('file_name')
        file_size = data.get('file_size')
        target_path = data.get('target_path')

        abs_path=os.path.join(self.main_path,target_path,file_name)

        '''文件是否存在，文件是否完整（断点续传），是否续传'''
        if os.path.exists(abs_path):
            file_has_size=os.stat(abs_path).st_size
            if file_has_size<file_size:
                #断点续传
                self.request.sendall('800'.encode('utf-8'))
            else:
                #文件完全存在
                self.request.sendall('801'.encode('utf-8'))
                return
        else:
            self.request.sendall('802'.encode('utf-8'))
            f=open(abs_path,'wb')

        while has_received<file_size:
            try:

                data=self.request.recv(1024)
            except Exception as e:
                break
            f.write(data)
            has_received+=len(data)

        f.close()

    def authenticate(self,user,pwd):

        cfg=configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)
        if user in cfg.sections():
            if cfg[user]['Password']==pwd:
                self.user=user
                #路径拼接，服务端的目录结构决定拼接的顺序及层级
                self.main_path=os.path.join(settings.BASE_DIR,'home',self.user)
                print('passion is complete')
                return user

    def ls(self,**data):

        file_list=os.listdir(self.main_path)

        file_str='\n'.join(file_list)
        print(file_str.encode('utf-8'))
        if not file_str:
            file_str='<empty dir>'.encode('utf-8')
        self.request.sendall(file_str.encode('utf-8'))

    def cd(self,**data):

        dir_name=data.get('dirname')

        if dir_name=='..':
            self.main_path=os.path.dirname(self.main_path)
        else:
            self.main_path=os.path.join(self.main_path,dir_name)

        self.request.sendall(self.main_path.encode('utf-8'))

    def mkdir(self,**data):

        dirname=data.get('dirname')
        path=os.path.join(self.main_path,dirname)

        if not os.path.exists(path):
            if '/' in dirname:
                os.makedirs(path)
            else:
                os.mkdir(path)
            self.request.sendall('creat success!'.encode('utf-8'))
        else:
            self.request.sendall('dirname exist'.encode('utf-8'))