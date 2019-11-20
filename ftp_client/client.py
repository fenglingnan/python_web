import optparse
import socket
import configparser
import json

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

class ClientHandler():

    def __init__(self):

        self.op=optparse.OptionParser()
        self.op.add_option('-s','--server',dest='server')
        self.op.add_option('-P', '--port', dest='port')
        self.op.add_option('-u', '--username', dest='username')
        self.op.add_option('-p', '--password', dest='password')

        self.opt,self.args=self.op.parse_args()
        self.verify_args(self.opt,self.args)
        self.run_connect()

    def verify_args(self,opt,args):

        server=opt.server
        port=opt.port
        # username=opt.username
        # password=opt.password

        if int(port)>0 and int(port)<65535:
            return True

        else:
            exit('port is in 0-65535')

    def run_connect(self):

        self.sock=socket.socket()
        print(self.opt)
        self.sock.connect((self.opt.server,int(self.opt.port)))

    def interactive(self):

        self.authenticate()

    def authenticate(self):

        if self.opt.username is None or self.opt.password is None:

            username=input('username:')
            password=input('password:')
            return self.get_auth(username,password)
        return self.get_auth(self.opt.username,self.opt.password)

    def get_data(self):

        data = self.sock.recv(1024).decode('utf-8')
        data = json.loads(data)
        return data

    def get_auth(self,user,pwd):

        data={
            'action':'auth',
            'username':user,
            'password':pwd
        }
        self.sock.send(json.dumps(data).encode('utf-8'))
        res=self.get_data()
        print(res['status_code'])
        if res['status_code']==254:
            self.user=user
            print(STATUS_CODE[254])
        else:
            print(STATUS_CODE[res['status_code']])

ch=ClientHandler()
ch.interactive()