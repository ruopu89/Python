# 思路：
#
# 先按照空格切分，然后一个个字符迭代，但如果发现是[或者"，则就不判断是否空格，直到]或者"结尾，这个区间获取的就是时间等数据。
#
# import datetime
#
#
# line = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
#
# CHARS = set(' \t')
# # print(CHARS)
# def makekey(line:str):
#     start = 0
#     skip = False
#     for i,c in enumerate(line):
#         if not skip and c in '"[':
#             start = i + 1
#             skip = True
#         elif skip and c in '"]':
#             skip = False
#             yield line[start:i]
#             start = i + 1
#             continue
#         if skip:
#             continue
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
# # print(list(makekey(line)))
# names = ('remote','','','datetime','request','status','length','','useragent')
#
# ops = (None,None,None,lambda timestr:datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M:%S %z'),lambda request:dict(zip(['method','url','protocol'],request.split())),int,int,None,None)
#
# def extract(line:str):
#     print(1, list(zip(names,makekey(line),ops)))
#     return dict(map(lambda item:(item[0],item[2](item[1]) if item[2] is not None else item[0]),zip(names,makekey(line),ops)))
#
# print(extract(line))

# =================================================================
# 正则表达式提取，使用命名分组
# import datetime
# import re
#
# line = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-"
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
#
# ops = {
#     'datetime':lambda timestr:datetime.datetime.strptime(tiemstr,'%d/%b/%Y:%H:%M:%S %z'),
#     'status':int,
#     'length':int
# }
#
# pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] \
# "(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/\d.]+)" \
# (?P<status>\d+) (?P<length>\d+) .+ "(?P<useragent>.+)"'''
#
# regex = re.compile(pattern)
#
# def extract(line:str) -> dict:
#     matcher = regex.match(line)
#     if matcher:
#         return {k:ops.get(k, lambda x:x)(v) for k,v in matcher.groupdict().items()}
#     else:
        # raise Exception('No match')9
#         return None
# print(extract(line))
# ============================================================================================
# 实例
import random
import time
import datetime
import re
from queue import Queue
import threading
# from collections import defaultdict
from pathlib import Path
from user_agents import parse
# pip install user-agents

logline = '''182.60.21.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

pattern = '''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" \
(?P<status>\d+) (?P<size>\d+) "[^"]+" "(?P<useragent>[^"]+)"'''

regex = re.compile(pattern)

ops = {
    'datetime':lambda timestr:datetime.datetime.strptime(timestr,"%d/$b/%Y:%H:%M:%S %z"),
    'status':int,
    'size':int,
    # 'request':lambda request:dict(zip(('method','url','protocol'),request.split())),
    'useragent':lambda useragent:parse(useragent)
}

def extract(line:str) -> dict:
    matcher = regex.match(line)
    if matcher:
        return {k:ops.get(k,lambda x:x)(v) for k,v in matcher.groupdict().items()}
    else:
        raise Exception('No match')

extract(logline)

def openfile(path:str):
    with open(str(path)) as f:
        for line in f:
            d = extract(line)
            if d:
                yield d
            else:
                continue

def load(*path):
    """文件装载"""
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

def window(src:Queue,handler,width:int,interval:int):
    start = datetime.datetime.strptime('1970/01/01 01:01:01 +0800', '%Y/%m/%d %H:%M:%S %z')
    current = datetime.datetime.strptime('1970/01/01 01:01:02 +0800', '%Y/%m/%d %H:%M:%S %z')
    delta = datetime.timedelta(seconds=width-interval)
    buffer = []
    while True:
        data = src.get()
        if data:
            buffer.append(data)
            current=data['datetime']

        if (current-start).total_seconds() >= interval:
            ret = handler(buffer)
            print(ret)
            start = current
            buffer = [i for i in buffer if i['datetime'] > current-delta]

def handler(iterable):
    return sum(map(lambda x:x['value'],iterable)) / len(iterable)

def donothing_handler(iterable:list):
    print(iterable)
    return iterable

def status_handler(iterable:list):
    status = {}
    for item in iterable:
        key = item['status']
        status[key] = status.get(key,0) + 1
        # if key not in d.keys():
        #     d[key] = 0
        # d[key] += 1
    # total = sum(d.values())
    total = len(iterable)
    return {k:status[k]/total*100 for k,v in status.items()}

allbrowsers = {}

# ua_dict = defaultdict(iterable:list)

# def browser_handler(iterable):
#     browsers = {}
#     for item in iterable:
#         ua = item['useragent']
#         key=(ua.browser.family,ua.browser.version_string)
#         browsers[key] = browsers.get(key,0) + 1
#         allbrowsers[key] = allbrowsers.get(key,0) + 1
#
#     print(sorted(allbrowsers.items(),key=lambda x:x[1],reverse=True)[:10])
#     return browsers

def dispatcher(src):
    handlers = []
    queues = []

    def reg(handler, width: int, interval: int):
        """
        注册 窗口处理函数

        :param handler: 注册的数据处理函数
        :param width: 时间窗口宽度
        :param interval: 时间间隔
        """
        q = Queue()
        queues.append(q)

        h = threading.Thread(target=window, args=(q, handler, width, interval))
        handlers.append(h)

    def run():
        for t in handlers:
            t.start()  # 启动线程处理数据

        for item in src:  # 将数据源取到的数据分发到所有队列中
            for q in queues:
                q.put(item)

    return reg, run

if __name__ == "main":
    import sys
    # path = sys.argv[1]
    path = '/media/shouyu/C64CC89B4CC8879F/works/马哥2018python/01.课堂笔记/p10c07/logs/test.log'
    reg, run = dispatcher(load(path))
    # dispatcher()返回的是reg和run函数，把这两个函数赋值给reg和run，下面再调用这两个函数并传参
    reg(donothing_handler, 10, 5)  # 注册处理函数
    # reg(browser_handler, 5, 5)
    run()  # 运行