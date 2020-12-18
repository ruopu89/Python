# from pathlib import Path
#
# p = Path('/tmp/test20200630.csv')
# parent = p.parent
# if not parent.exists():
#     parent.mkdir(parents=True)
#
# csv_body = '''\
# id,name,age,comment
# 1,zs,18,"I'm 18"
# 2,ls,20,"this is a ""test""string."
# 3,ww,23,"你好
#
# 计算机
# "
# '''
# p.write_text(csv_body)
#
# import csv
#
# p = Path('/tmp/test20200630.csv')
# with open(str(p)) as f:
#     reader = csv.reader(f)
#     print(next(reader))
#     print(next(reader))
#
# rows = [
# 	[4,'tom',22,'tom'],
# 	(5,'jerry',24,'jerry'),
# 	(6,'justin',22,'just\t"in'),
# 	"abcdefghi",
# 	((1,),(2,))
# ]
#
# row = rows[0]
# with open(str(p), 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(row)
#     writer.writerows(rows)
# ===================================================
# 处理ini文件
from configparser import ConfigParser

filename = '/tmp/test.ini'
newfilename = '/tmp/mysql.ini'

cfg = ConfigParser()
cfg.read(filename)
# print(cfg.sections())
# print(cfg.has_section('client'))
#
# print(cfg.items('mysqld'))
# for k,v in cfg.items():
    # print(k, type(v))
    # print(k, cfg.items(k))
#
# tmp = cfg.get('mysqld','port')
# print(type(tmp), tmp)
# print(cfg.get('mysqld', 'a'))
# print(cfg.get('mysqld', 'magedu', fallback='python'))
#
# tmp = cfg.getint('mysqld', 'port')
# print(type(tmp), tmp)
#
if cfg.has_section('test'):
    cfg.remove_section('test')

cfg.add_section('test')
cfg.set('test', 'test1', '1')
cfg.set('test', 'test2', '2')

with open(newfilename, 'w') as f:
    cfg.write(f)

# print(cfg.getint('test', 'test2'))
cfg.remove_option('test', 'test2')

cfg['test']['x'] = '100'
cfg['test2'] = {'test2':'1000'}

# print('x' in cfg['test'])
# print('x' in cfg['test2'])
#
print(cfg._dict)
#
# with open(newfilename, 'w') as f:
#     cfg.write(f)