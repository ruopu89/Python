# 简单程序
# import argparse
#
# parser = argparse.ArgumentParser(prog='ls',add_help=True,description='list diretory contents')
# args = parser.parse_args()
# parser.print_help()
# ===================================================
# import argparse
#
# parser = argparse.ArgumentParser(prog='ls',add_help=True,description='list directory contents')
# parser.add_argument('path')
# args = parser.parse_args()
# parser.print_help()
# ======================================================
# 选项参数实现
# import argparse
#
# parser = argparse.ArgumentParser(prog='ls',add_help=True,description='list directory contents')
# parser.add_argument('path',nargs='?',default='.',help="directory")
# parser.add_argument('-l',action='store_true',help='use a long listing format')
# parser.add_argument('-a','--all',action='store_true',help='show all files, do not ignore entries starting with.')
# args = parser.parse_args('-l -a /tmp'.split())
# print(args)
# parser.print_help()
# ========================================================
# ls 业务功能实现
# import argparse
# from pathlib import Path
# from datetime import datetime
#
# parser = argparse.ArgumentParser(prog='ls',add_help=True,description='list directory contents')
# parser.add_argument('path',nargs='?',default='.',help="directory")
# parser.add_argument('-l',action='store_true',help='use a long listing format')
# parser.add_argument('-a','--all',action='store_true',help='show all files, do not ignore entries starting with.')
#
#
# args = parser.parse_args()
# print(1, args.path,args.all, "args:{}".format(args))
# parser.print_help()
#
# # def listdir(path, all=False):
# #     p = Path(path)
# #     for i in p.iterdir():
# #         if not all and i.name.startswith('.'):
# #             continue
# #         yield i.name
# #
# # print(list(listdir((args.path))))
#
# def _getfiletype(f:Path):
#     if f.is_dir():
#         return 'd'
#     elif f.is_block_device():
#         return 'b'
#     elif f.is_char_device():
#         return 'c'
#     elif f.is_socket():
#         return 's'
#     elif f.is_symlink():
#         return 'l'
#     else:
#         return '-'
#
# modelist = dict(zip(range(9),['r','w','x','r','w','x','r','w','x']))
# def _getmodestr(mode:int):
#     m = mode & 0o777
#     mstr = ''
#     for i in range(8,-1,-1):
#         if m >> i & 1:
#             mstr += modelist[8-i]
#         else:
#             mstr += '-'
#     return mstr
#
# def listdir(path, all=False, detail=False):
#     """详细列出本目录"""
#     p = Path(path)
#     for i in p.iterdir():
#         if not all and i.name.startswith('.'):
#             print(11111)
#             continue
#         if not detail:
#             print(22222)
#             yield (i.name,)
#             # return (i.name,)
#         else:
#             print(33333)
#             stat = i.stat()
#             # print(1, stat)
#         # t = _getfiletype(i)
#         #     mode = oct(stat.st_mode)[-3:]
#             mode = _getfiletype(i)  + _getmodestr(stat.st_mode)
#         #     mode = _getmodestr(stat.st_mode)
#         #     mode = _getfiletype(i)
#             atime = datetime.fromtimestamp(stat.st_atime).strftime('%Y %m %d %H:%M:%S')
#             yield mode,stat.st_uid,stat.st_gid,stat.st_size,atime,i.name
#             # print(mode, stat.st_uid, stat.st_gid, stat.st_size, atime, i.name)
#             # return mode, stat.st_uid, stat.st_gid, stat.st_size, atime, i.name
#
# # print(list(listdirdetail(args.path)))
# # for x in listdir(args.path, detail=True):
# #     print(next(x))
#
# sorted(listdir(args.path, detail=True), key=lambda x: x[len(x) - 1])
# # print(listdir(args.path,all=True,detail=True))
# # print(next(listdir(args.path,all=True,detail=True)))
#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     print(args)
#     parser.print_help()
#     files = listdir(args.path, args.all, args.l)
#     print(list(files))
# ================================================================
# return 测试
# def test_return(x):
#     if x > 0:
#         yield x
#     else:
#         return 0
# print('x',test_return(0))
# 测试没发现上面不打印内容的情况。
# ================================================================
# 最终代码
import argparse
import stat
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(prog='ls',description='list directory contents',add_help=False)
parser.add_argument('path',nargs='?',default='.',help="directory")
parser.add_argument('-l',action='store_true',help='use a long listing format')
parser.add_argument('-a','--all',action='store_true',help='show all files, do not ignore entries starting with.')
parser.add_argument('-h','--human-readable',action='store_true',help='with -l, print sizes in human readable format')

def listdir(*path,all=False,detail=False,human=False):
    def _gethuman(size:int):
        units = ' KMGTP'
        depth = 0
        while size >= 1000:
            size = size // 1000
            depth += 1
        return '{}{}'.format(size,units[depth])

    def _listdir(*path,all=False,detail=False,human=False):
        """详细列出本目录"""
        p = Path(path)
        for i in p.iterdir():
            if not all and i.name.startswith('.'):
                continue
            if not detail:
                yield (i.name,)
            else:
                st = i.stat()
                mode = stat.filemode(st.st_mode)
                atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                size = str(st.st_size) if not human else _gethuman(st.st_size)
                yield (mode,st.st_nlink,st.st_uid,st.st_gid,size,atime,i.name)

    yield from sorted(_listdir(path, all, detail, human), key=lambda x:x[len(x)-1])

if __name__ == '__main__':
    args = parser.parse_args()
    print(1, args)
    parser.print_help()
    # files = listdir(args.path, args.all,args.l,args.human_readable)
    files = listdir('/home/shouyu/','/home', detail=True, human=True)
    for i in files:
        print(i)





