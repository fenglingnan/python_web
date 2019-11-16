
import socketserver
import optparse

from conf import settings
from core import server

class ArgvHandler():
    def __init__(self):

        self.op=optparse.OptionParser()
        #从配置文件中取
        # self.op.add_option('-s','--server',dest='server')
        # self.op.add_option('-P', '--port', dest='server')

        options,args=self.op.parse_args()
        #options是class，不是一个字典

        self.verify(options,args);

    def verify(self,options,args):

        cmd=args[0]

        if hasattr(self,cmd):

            func=getattr(self,cmd);
            func()

    def start(self):
        print('server is working...')
        s=socketserver.ThreadingTCPServer((settings.IP,settings.PORT),server.ServerHandler)
        s.serve_forever()

    def help(self):
        pass