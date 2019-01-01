"""
破解有道词典
"""
from urllib import request,parse

def youdao(key):
    url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data={
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1540793706406",
        "sign": "a512d22ee34e1deb69e46d72de43f172",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    #参数data需要是bytes格式
    data=parse.urlencode(data).encode()
    headers={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN, zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "200",
        "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1459785113.7807143; _ga=GA1.2.5475587.1533802897; OUTFOX_SEARCH_USER_ID=-888815437@10.169.0.84; JSESSIONID=aaa4h0axAeQ7Y59A809Aw; ___rl__test__cookies=1540793706402",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }
    req=request.Request(url=url,data=data,headers=headers)
    rsp=request.urlopen(req)
    html=rsp.read().decode()
    print(html)
youdao('girl')
if __name__=='__mian__':
    pass

