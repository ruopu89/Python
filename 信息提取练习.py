# import datetime

# line = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-"
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
#
# CHARS = set(" \t")
#
#
# def makekey(line:str):
#     start = 0
#     skip =False
#     for i,c in enumerate(line):
#         if not skip and c in '"[':
#             start = i + 1
#             skip = True
#         elif skip and c in '"]':
#             skip = False
#             yield line[start:i]
#             start = i + 1
#             continue
#
#         if skip:
#             continue
#
#         if c in CHARS:
#             if start == i:
#                 start = i + 1
#                 continue
#             yield line[start:i]
#             start = i + 1
#     else:
#         if start < len(line):
#             yield line[start:]
#
# names = ('remote','','','datetime','request','status','length','','useragent')
#
# ops = (None,None,None,lambda timestr:datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
#       lambda request: dict(zip(['method','url','protocol'],request.split())),
#       int,int,None,None
#       )
#
# def extract(line:str):
#     return dict(map(lambda item:(item[0],item[2](item[1]) if item[2] is not None else item[1]),zip(names,makekey(line),ops)))
#
# print(extract(line))


# names = ('remote','','','datetime','request','status','length','','useragent')

# import datetime
# import re
# from queue import Queue
# import threading
# from pathlib import Path
# from collections import defaultdict
# from user_agents import parse
#
#
# line = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

# ops = {
#     # 'remote':str,
#     'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
#     'status':int,   # 用int函数处理数据。因为默认是字符串格式 ，所以这里要用int处理一下
#     'length':int,
#     'request':lambda request:dict(zip(('method','url','protocol'),request.split())),
#     'useragent':lambda useragent:parse(useragent)
# }


# pattern='''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "[^"]+" "(?P<useragent>[^"]+)"'''
# # pattern='''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "[^"]+" "(?P<useragent>[^"]+)"'''
# regex = re.compile(pattern)

# def extract(line):
#     matcher = regex.match(line)
#     # return matcher.groupdict()
#     # print(type(matcher))
#     # print(matcher,'***')
#     if matcher:
#         return {k:ops.get(k, lambda x:x)(v) for k,v in matcher.groupdict().items()}
#     else:
#         raise Exception('No match')
    # for k, v in matcher.groupdict().items():
    #     print(ops.get(k),'!!!')

# print(extract(line))
# print(matcher.get())
# 下面输出的就是src：
# {'remote': '182.60.21.153', 'datetime': datetime.datetime(2013, 2, 19, 10, 23, 29, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800))), 'request': {'method': 'GET', 'url': '/o2o/media.html?menu=3', 'protocol': 'HTTP/1.1'}, 'status': 200, 'size': '16691', 'useragent': <user_agents.parsers.UserAgent object at 0x7fee04fa0370>}

# print(extract(line))
# def openfile(path:str):
#     with open(str(path)) as f:
#         for line in f:
#             d = extract(line)
#             if d:
#                 yield d
#             else:
#                 continue


# def load(*path):
#     for file in path:
#         p = Path(file)
#         if not p.exists():
#             continue
#         if p.is_dir():
#             for x in p.iterdir():
#                 if x.is_file():
#                     yield from openfile(str(x))
#         elif p.is_file():
#             yield from openfile(str(p))

# # for i in load('test.log'):
# #     print(i)
#
# def window(src, handler, width:int, interval:int):
#     start = datetime.datetime.strptime('1970/01/01 01:00:00 +0800', '%Y/%m/%d %H:%M:%S %z')
#     current = datetime.datetime.strptime('1970/01/01 01:01:01 +0800', '%Y/%m/%d %H:%M:%S %z')
#     delta = datetime.timedelta(seconds=width - interval)
#     # delta = width - interval
#
#     # print(start,current,)
#     buffer = []
#     # [{'remote': '196.52.43.60',
#     #   'datetime': datetime.datetime(2017, 4, 18, 10, 55, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800))),
#     #   'request': {'method': 'GET', 'url': '/', 'protocol': 'HTTP/1.1'}, 'status': 301, 'size': '278', 'useragent': '-'},
#     #  {'remote': '42.120.74.236',
#     #   'datetime': datetime.datetime(2017, 4, 18, 11, 3, 4, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800))),
#     #   'request': {'method': 'GET', 'url': '/', 'protocol': 'HTTP/1.1'}, 'status': 200, 'size': '8416',
#     #   'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}]
#     # for data in src:
#     while True:
#         data = src.get()
#         # print(src,'@@@')
#         # print(data,'###')
#         if data:
#             # print(data,'!!!')
#             buffer.append(data)
#             # print(buffer)
#             current = data['datetime']
#             # print(current)
#
#         # if (current - start).total_seconds() >= interval:
#         if (current-start).total_seconds() >= interval:   # 什么时候处理buffer数据
# # 当现在的时间减去开始时间大于等于间隔时间时就处理一下buffer中的数据，第一次处理数据时因为start和current都设置成了1970年，
# # 所以buffer中存储一条data数据后就会对buffer数据进行处理，之后buffer中会存储两条数据才被处理
#
#             ret = handler(buffer)
#             print(ret)
#
#             start = current
#
#             buffer = [i for i in buffer if i['datetime'] > current - delta]
#
# def donothing_handler(iterable:list):
#     print(iterable)
#     return iterable
#
# # window(load('test.log'), donothing_handler, 10, 5)
#
#
#
# def status_handler(iterable:list):   # 统计状态码
#     d = {}
#     for item in iterable:
#         key = item['status']
#         if key not in d.keys():
#             d[key] = 0
#         d[key] += 1
#     total = sum(d.values())
#     # print(d,'!!!')
#     # print(total,'@@@')
#     # {200: 46, 500: 1} !!!
#     # 47 @ @ @
#     # {200: 97.87234042553192, 500: 2.127659574468085}
#     # {200: 3, 301: 1} !!!
#     # 4 @ @ @
#     # {200: 75.0, 301: 25.0}
#     # {200: 1} !!!
#     # 1 @ @ @
#     # {200: 100.0}
#
#     return {k:v/total*100 for k,v in d.items()}
#
# ua_dict = defaultdict(lambda :0)
#
# def browser_handler(iterable:list):   # 统计浏览器的情况
#     for item in iterable:
#         ua = item['useragent']
#         key = (ua.browser.family, ua.browser.version_string)
#         ua_dict[key] += 1
#     return ua_dict
#
# def dispatcher(src):
#     queues = []
#     threads = []
#
#     def reg(handler, width, interval):   # 在这里注册
#         q = Queue()
#         queues.append(q)
#         t = threading.Thread(target=window, args=(q, handler, width, interval))
#         threads.append(t)
#
#     def run():   # 在这里真正运行
#         for t in threads:
#             t.start()
#
#         for x in src:
#             for q in queues:
#                 q.put(x)
#
#     return reg,run
#
# reg,run = dispatcher(load('test.log'))
#
# # reg(donothing_handler, 10, 5)
# reg(status_handler, 5, 5)
# # reg(browser_handler, 5, 5)
# run()
# # window(load('test.log'),donothing_handler,10,5)
# # for i in load("test.log"):
# #     print(i)



#1

import datetime
import re
from pathlib import Path
from queue import Queue
import threading
from collections import defaultdict
from user_agents import parse

ops = {
    'datetime':lambda timestr:datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M:%S %z'),
    'status':int,
    'length':int,
    'request':lambda request:dict(zip(('method','url','protocol'),request.split())),
    'useragent':lambda useragent:parse(useragent)
}

pattern = '''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "[^"]+" "(?P<useragent>[^"]+)"'''

regex = re.compile(pattern)

# extract函数是为了将简单的字符串转化为字典并返回
def extract(line):
    matcher = regex.match(line)
    if matcher:
        return {k:ops.get(k, lambda x:x)(v) for k,v in matcher.groupdict().items()}
    else:
        raise Exception('No match')

# 逐行处理日志文件，把一行日志给extract处理成字典并惰性返回extract的处理结果，也就是每次返回一行字典
def openfile(path:str):
    with open(str(path)) as f:
        for line in f:
            d = extract(line)
            if d:
                yield d
            else:
                continue

# 处理多个文件，判断是目录还是文件，只处理一层目录，最后都要按文件交给openfile函数处理
def load(*path):
    for file in path:
        p = Path(file)
        if not p.exists():
            continue
        if p.is_dir():
            for x in p.iterdir():
                if x.is_file():
                    yield from openfile(str(x))
        elif p.is_file():
            yield from openfile(str(p))

def window(src, handler, width:int, interval:int):
    start = datetime.datetime.strptime('20170101 00:00:01 +0800','%Y%m%d %H:%M:%S %z')
    current = datetime.datetime.strptime('20170101 00:00:02 +0800', '%Y%m%d %H:%M:%S %z')
    delta = datetime.timedelta(seconds=width - interval)

    buffer = []

    while True:
        data = src.get()
        if data:
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print(ret)
            start = current
            buffer = [i for i in buffer if i['datetime'] > current - delta]

def donothing_handler(iterable:list):
    print(iterable)
    return(iterable)

def status_handler(iterable:list):
    d = {}
    for item in iterable:
        key = item['status']
        if key not in d.keys():
            d[key] = 0
        d[key] += 1
    total = sum(d.values())
    return {k:v/total*100 for k,v in d.items()}

ua_dict = defaultdict(lambda :0)
def browser_handler(iterable:list):
    for item in iterable:
        ua = item['useragent']
        key = (ua.browser.family, ua.browser.version_string)
        ua_dict[key] += 1
    return ua_dict

def dispatcher(src):
    queues = []
    threads = []

    def reg(handler, width, interval):
        q = Queue()
        queues.append(q)
        t = threading.Thread(target=window, args=(q, handler, width, interval))
        threads.append(t)

    def run():
        for t in threads:
            t.start()
        for x in src:
            for q in queues:
                q.put(x)
    return reg,run

reg,run = dispatcher(load('test.log'))
# reg(donothing_handler, 10, 5)
# reg(status_handler, 5, 5)
reg(browser_handler, 5, 5)
run()
