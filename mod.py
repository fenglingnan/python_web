import sys
# print(sys.argv)
# command=sys.argv[1]
# path=sys.argv[2]
# if command=='post':
#     pass
# elif command=='get':
#     pass
# sys.stdout.write('#')
import time
import json
# for  i in range(100):
#     time.sleep(0.1)
#     sys.stdout.write('#')
#     sys.stdout.flush()
dic={'name':'alex'}
data=json.dumps(dic)
print(data,type(data))
print(json.loads(data),type(json.loads(data)))
#注意格式一定要双引号，json得格式
import xml.etree.cElementTree as ET
tree=ET.parse('data.xml');
print(tree)#tag标签名，attrib属性值同js得attribute，text取标签间得文本
s='avavavaalexdvavadvad'
print(s.find('alex'))