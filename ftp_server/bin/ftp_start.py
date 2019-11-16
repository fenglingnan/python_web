import os,sys

#添加环境变量
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from core import main

if __name__ == '__main__':
    main.ArgvHandler()