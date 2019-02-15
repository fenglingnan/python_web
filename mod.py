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
import re
res=re.findall('\d+','vadkvabouvy348914y1903fhvajkdv12312dvadvad');
print(res)
print(re.findall('alex','aelexakdvjbadiovbad'))
print(re.findall("a..x",'vakjvazvjadjkbvxaddx'))
print(re.findall('^a..x','assxadvxadv'))
print(re.findall('a..x','assxadvxadv'))
print(re.findall('a..x$','assxadvxadavvx'))
print(re.findall('a..x\$$','assxadvxadavvx$'))
print(re.findall('d*','assxadvxadavvx$dd'))
print(re.findall('d+','assxadvxadavvx$dd'))
print(re.findall('alex+','alvalexxxxvakdjbv'))
print(re.findall('alex*','alvalevakdjbv'))
print(re.findall('alex+','alvalevakdjbv'))
print(re.findall('alex?','alvalexxvakdjbv'))
print(re.findall('alex?','alvalevakdjbv'))
print(re.findall('alex{6}','alvalexxxxxxxxvakdjbv'))
print(re.findall('alex+?','alvalexxxxxxxxvakdjbv'))
"""
    ^表示字符开头，
    $表示字符结尾，
    *表示0到无穷个，
    +表示1到无穷个，
    ？表示0，1次,
    一个.只匹配一个字符
    加上？变成惰性匹配，按最小匹配
    {}  ==> {0,}==*
        {1,}==+
        {0,1}==?
        可表示所有
    []表示里面的内容是或,[]里的^表示非，[^0-9]表示非0-9的字符，-表示范围，\表示转义
    \d表示[0,9]
    \D表示[^0-9]
    \s匹配任何空白字符==[\t\n\r\f\v]
    \S==[^\t\n\r\f\v]
    \w==[a-zA-Z0-9_]
    \W==[^a-zA-Z0-9_]
    \b匹配特殊字符边界，如空格，#，&等
    ()表示整体
"""
print(re.findall("www[oldboy baidu]",'wwwbaidu'))
print(re.findall('x[yz]p','xypzzxczxzpczcz'))
print(re.findall('q[a-z]','qf'))
print(re.findall('q[^a-z]+','q12f'))
#12+(34*6+2-5*(2-1)), 匹配2-1
print(re.findall("\([^()]+\)","12+(34*6+2-5*(2-1))"))
print(re.findall("\d+","12+(34*6+2-5*(2-1))"))
print(re.findall('I\\b','hello,I am CHINESE'))
print(re.findall(r'I\b','hello,I am CHINESE'))
print(re.findall(r'c\\l','abc\lqeg'))
print(re.findall('c\\\\l','abc\lqeg'))#两层转义，re的转义和python解释器的转义
print(re.findall('k[a\|b]','ka|kbc\lqeg'))
print(re.findall('(abc)+','abcccc'))
print(re.findall('(?:abc)+','abcabcabc'))
print(re.findall('(?P<name>\w+)','abcccc'))
print(re.search('(?P<name>\w+)','abcccc'))#search只找一个就停止
print(re.search('(?P<name>\w+)','abcccc').group())
print(re.search('(?P<name>[a-z]+)\d+','alex34cx22jx23').group())
print(re.search('(?P<name>[a-z]+)\d+','alex34cx22jx23').group('name'))
print(re.search('(?P<name>[a-z]+)(?P<age>\d+)','alex34cx22jx23').group('age'))
print(re.match('\d+','ad23'))#math只匹配开始位置，search替代
print(re.match('\d+','23ad23'))
print(re.split('[ |]','hello world|lin'))#split不是一次性全分割完，匹配成功分割一次
print(re.split('[ab]','asdabcd'))
print(re.sub('\d','A','222avaodvhad'))#替换，数字参数是次数
print(re.sub('\d','A','222avaodvhad',2))
print(re.subn('\d','A','222avaodvhad5'))
com=re.compile('\d+')#同js的reg
print(com.findall('198hf198eh'))
ne=re.finditer('\d+','09uva209duva09dv09')#findall迭代器版本
print(ne)
print(next(ne).group())
print(next(ne).group())
print(ne.__next__().group())
print(re.findall('http://www\.(baidu|163)\.com','vadvadvhttp://www.baidu.comvdadvad'))#优先匹配分组里的内容
print(re.findall('http://www\.(?:baidu|163)\.com','vadvadvhttp://www.baidu.comvdadvad'))#?:去除优先级