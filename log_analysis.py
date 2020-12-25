import datetime
import re
from pathlib import Path
from queue import Queue
import threading
from collections import defaultdict
from user_agents import parse

ops = {
    'datetime':int,
    'status':int,
    'length':int,
    'request':lambda request:dict(zip(('method','url','protocol'),request.split())),
    'useragent':lambda useragent:parse(useragent)
}

pattern = '''(?P<remote>[\d\.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "(?P<response>\w)" "(?P<other>\w)"'''

regex = re.compile(pattern)

# extract函数是为了将简单的字符串转化为字典并返回
def extract(line):
    matcher = regex.match(line)
    if matcher:
        return {k:ops.get(k, lambda x:x)(v) for k,v in matcher.groupdict().items()}
    else:
        raise Exception('No match')




# varnishncsa.log-2020-03-16
with open('varnishncsa.log-2020-03-16') as f:
    for line in f:
        if
        print(line)
