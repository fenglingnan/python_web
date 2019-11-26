import optparse
import socket
import configparser
import json
import os,sys

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
        # self.last = 0
        self.op.add_option('-s','--server',dest='server')
        self.op.add_option('-P', '--port', dest='port')
        self.op.add_option('-u', '--username', dest='username')
        self.op.add_option('-p', '--password', dest='password')
        self.current=''
        self.opt,self.args=self.op.parse_args()
        self.verify_args(self.opt,self.args)
        self.run_connect()
        self.main_path=os.path.dirname(os.path.abspath(__file__))

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
        if self.authenticate():
            print('begin to interactive')
            cmd_info=input('[%s]'%self.current).strip()#put
            cmd_list=cmd_info.split()

            if hasattr(self,cmd_list[0]):
                func=getattr(self,cmd_list[0])
                func(cmd_list)

    def put(self,*cmd_list):

        # print(cmd_list)
        #put 12.png image 返回的是一个元组，注意索引cmd_list不是一个单独数组
        action,local_path,target_path=cmd_list[0]

        local_path=os.path.join(self.main_path,local_path)
        file_name=os.path.basename(local_path);
        file_size=os.stat(local_path).st_size

        data={
            'action':'put',
            'file_name':file_name,
            'file_size':file_size,
            'target_path':target_path
        }
        self.sock.send(json.dumps(data).encode('utf-8'))
        is_exist=self.sock.recv(1024).decode('utf-8')
        has_sent=0
        if is_exist=='800':
            #文件不完整
            pass
        elif is_exist=='801':
            #文件完全存在
            return
        else:
            pass

        f=open(local_path,'rb')
        while has_sent<file_size:
            data=f.read(1024)
            self.sock.sendall(data)
            has_sent+=len(data)
            self.show_progress(has_sent,file_size)
        f.close()

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
            self.current=user
            print(STATUS_CODE[254])
            return True
        else:
            print(STATUS_CODE[res['status_code']])

    def show_progress(self,has,total):

        rate=float(has)/float(total)
        rate_num=int(rate*100)
        # if self.last!=rate_num:
        sys.stdout.write('%s%% %s\r'%(rate_num,'#'*rate_num))
        # self.last=rate_num

    def ls(self,*cmd_list):

        data={"action":"ls"}
        print(json.dumps(data).encode('utf-8'))
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data=self.sock.recv(1024).decode('utf-8')
        print(data)

    def cd(self,*cmd_list):

        # print(cmd_list)
        # 解析似乎和教程不太一样
        data={
            'action':'cd',
            'dir_name':cmd_list[0][1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(os.path.basename(data))
        self.current=os.path.basename(data)

    def mkdir(self,*cmd_list):

        data={
            'action':'mkdir',
            'dirname':cmd_list[0][1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))

ch=ClientHandler()
ch.interactive()