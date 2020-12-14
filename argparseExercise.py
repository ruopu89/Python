# 实现ls命令功能，实现-l、-a和--all、-h选项
# 实现显示路径下的文件列表
# -a和--all显示包含开头的文件
# -l详细列表显示
# -h和-l配合，人性化显示文件大小，例如1K、1G、1T等，可以认为1G=1000M
# c字符；d目录；-普通文件；l软链接；b块设备；s socket文件；p pipe文件，即FIFO
# -rw-rw-r--   1    python    python    5  Oct  25  00:07  test4
# mode       硬链接  属主        属组     字节 时间             name
# 按照文件名排序输出，可以和ls的顺序不一样，但要求文件名排序
# 要求详细列表显示时，时间可以按照"年-月-日 时:分:秒"  格式显示

# 1. 先定义一个命令，命令的名称，有哪些参数
# 2. 再定义listdir函数，设置参数有path表示路径，all表示是否显示隐藏文件，detail表示是否显示全部信息，human表示是否显示大小
# 3. 定义子函数_gethuma，设置一个参数size，传入的只是字节，所以下面要对传入的字节进行单位转换
# 4. 定义子函数_listdir，设置参数path表示路径，all表示是否显示隐藏文件，detail表示是否显示全部信息，human表示是否显示大小，后三项默认是False
# 先将path传入的路径给p，之后迭代p这个路径，如果传入的all参数是False并且迭代的路径的名称是以点开头的，那么就跳过本次循环。如果传入的detail是False，
# 也就是没有转入detail参数，而是使用了默认参数，就返回路径名称。如果传入的detail值是True，就要显示详细信息。先把路径的所有信息给st变量
# ，再从st变量中取出路径的权限，访问时间，大小，最后惰性返回详细信息
# 5. 排序输出


# import argparse
# import stat
# from pathlib import Path
# from datetime import datetime
#
#
#
# def listdir(path,all=False,detail=False,human=False):
#     def _gethuman(size: int):
#         units = ' KMGTP'
#         depth = 0
#         while size >= 1000:
#             size = size // 1000
#             depth += 1
#         return '{}{}'.format(size,units[depth])
#
#     def _listdir(path, all=False, detail=False, human=False):
#         """详细列出本目录"""
#         p = Path(path)
#         for i in p.iterdir():
#             if not all and i.name.startswith('.'):
#                 continue
#             if not detail:
#                 yield (i.name,)
#             else:
#                 st = i.stat()
#                 mode = stat.filemode(st.st_mode)
#                 atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
#                 # size = str(st.st_size) if not human else _gethuman(st.st_size)
#                 size = int(st.st_size) if not human else _gethuman(int(st.st_size))
#
#
#                 yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
#
#     # yield from sorted(_listdir(path, all, detail, human), key=lambda x:x[len(x) - 1])
#     yield from sorted(_listdir(path, all, detail, human), key=lambda x:x[4])
#
#
# parser = argparse.ArgumentParser(prog='ls',description='list directory contents',add_help=False)
# parser.add_argument('path',nargs='?',default='.',help="directory")
# parser.add_argument('-h',action='store_true',help='use a long listing format')
# parser.add_argument('-a','--all',action='store_true',help='show all files, do not ignore entries starting with .')
# parser.add_argument('-l','--human-readable',action='store_true',help='with -l, print sizes in human readable format')
#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     print(args)
#     parser.print_help()
#     files = listdir(args.path, args.all, args.l, args.human_readable)
#     # print(list(files))
#     print(next(files))



# 1

# import argparse
# import stat
# from pathlib import Path
# from datetime import datetime
#
# parser = argparse.ArgumentParser(prog='ls',description='list directory contents', add_help=False)
# parser.add_argument('path',nargs='?',default='.',help='directory')
# parser.add_argument('-h','--help',action='store_true',help='use a long listing format')
# parser.add_argument('-a','--all',action='store_true',help='show all files, do not ignore entries starting with. ')
# parser.add_argument('-l','--human-readable',action='store_true',help='with -l, print sizes in human readable format')
#
# def listdir(path,all=False,detail=False,human=False):
#     def _gethuman(size:int):
#         units = ' KMGTP'
#         depth = 0
#         while size >= 1000:
#             size = size // 1000
#             depth += 1
#         return '{}{}'.format(size,units[depth])
#
#     def _listdir(path,all=False,detail=False,human=False):
#         """详细列出本目录"""
#         p = Path(path)
#         for i in p.iterdir():
#             if not all and i.name.startswith('.'):
#                 continue
#             if not detail:
#                 yield (i.name,)
#             else:
#                 st = i.stat()
#                 mode = stat.filemode(st.st_mode)
#                 atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
#                 size = str(st.st_size) if not human else _gethuman(st.st_size)
#
#             yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
#
#     yield from sorted(_listdir(path,all,detail,human),key=lambda x:x[-1])
#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     print(args)
#     # parser.print_help()
#     files = listdir(args.path, args.all, args.help, args.human_readable)
#     print(next(files))


# 2

# 1. 导入模块
# 2. 定义参数
# 3. 定义函数，逻辑是先定义获取文件大小的子函数；再定义获取文件信息的子函数。获取文件大小的子函数通过与1000整除得到文件大小的单位；获致文件信
# 息的子函数通过传入的几个参数进行判断，如是否有路径，没有就使用默认的当前路径；all是否为False，如果为False并且文件是以点开头的文件，就跳出
# 本轮循环；如果为True，就再判断传入的human是否为False，如果为False就显示文件的名称，如果为True就显示文件的详细信息。
# 4. 最后返回按文件名排序后的结果
#
# import stat
# from pathlib import Path
# from datetime import datetime
# import argparse
#
# parser = argparse.ArgumentParser(prog='ls',description='list directory contents',add_help=False)
# parser.add_argument('path',nargs='?',default='.',help='directory')
# parser.add_argument('-a','--all',action='store_true',help='show all files, do not ignore entries starting with .')
# parser.add_argument('-h','--human-readable',action='store_true',help='with -l, print sizes in human readable format')
# parser.add_argument('-l',action='store_true',help='use a long listing format')
#
# def listdir(path,all=False,detail=False,human=False):
#     def _gethuman(size:int):
#         units = ' KMGTP'
#         depth = 0
#         while size >= 1000:
#             size = size // 1000
#             depth += 1
#         return '{}{}'.format(size,units[depth])
#     def _listdir(path,all=False,detail=False,human=False):
#         p = Path(path)
#         for i in p.iterdir():
#             if not all and i.name.startswith('.'):
#                 continue
#             if not human:
#                 yield (i.name,)
#             else:
#                 st = i.stat()
#                 mode = stat.filemode(st.st_mode)
#                 atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
#                 size = str(st.st_size) if not human else _gethuman(st.st_size)
#                 yield (mode,st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
#
#     yield from sorted(_listdir(path, all, help, human), key=lambda x:x[-1])
#
#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     print(args)
#     # parser.print_help()
#     files = listdir(args.path, args.all, args.l, args.human_readable)
#     print(list(files))



# 3
# import stat
# import argparse
# from datetime import datetime
# from pathlib import Path
#
# parser = argparse.ArgumentParser(prog='ls',description='list directory contents',add_help=True)
# parser.add_argument('path',nargs='?',default='.',help='directory')
# parser.add_argument('-a','--all',action='store_true',help='show all files, do not ignore entries starting with .')
# parser.add_argument('-l','--detail',action='store_true',help='use a long listing format')
# parser.add_argument('-v','--human_readable',action='store_true',help='print sizes in human readable format')
#
# def listdir(path,all=False,detail=False,human=False):
#     def _gethuman(size:int):
#         units = ' KMGTP'
#         depth = 0
#         while size >= 1000:
#             size = size // 1000
#             depth += 1
#         return '{}{}'.format(size,units[depth])
#     def _listdir(path,all=False,detail=False,human=False):
#         p = Path(path)
#         for i in p.iterdir():
#             if not all and i.name.startswith('.'):
#                 continue
#             if not human:
#                 yield (i.name,)
#             else:
#                 st = i.stat()
#                 mode = stat.filemode(st.st_mode)
#                 atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
#                 size = str(st.st_size) if not human else _gethuman(st.st_size)
#                 yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
#     yield from sorted(_listdir(path, all, detail, human), key=lambda x:x[-1])
#
#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     print(args)
#     parser.print_help()
#     files = listdir(args.path, args.all, args.detail, args.human_readable)
#     print(next(files))

# 4
# import stat
# import argparse
# from datetime import datetime
# from pathlib import  Path
#
# parser = argparse.ArgumentParser(prog='ls',description='list directory contents',add_help=True)
# parser.add_argument('path',nargs='?',default='.',help='directory')
# parser.add_argument('-a',action='store_true',help='all show')
# parser.add_argument('-l',action='store_true',help='show common file')
# parser.add_argument('-v',action='store_true',help='show detailed information')
#
# def listdir(path, all=False, detail=False, human=False):
#     def _gethuman(size:int):
#         units = ' KMGTP'
#         depth = 0
#         while size >= 1000:
#             size = size // 1000
#             depth += 1
#         return '{}{}'.format(size,units[depth])
#     def _listdir(path, all=False, detail=False, human=False):
#         p = Path(path)
#         for i in p.iterdir():
#             if not all and i.name.startswith('.'):
#                 continue
#             if not human:
#                 yield (i.name)
#             else:
#                 st = i.stat()
#                 mode = stat.filemode(st.st_mode)
#                 atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:$S')
#                 size = str(st.st_size) if not human else _gethuman(st.st_size)
#                 yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
#     yield from sorted(_listdir(path, all, detail, human),key=lambda x:x[-1])
#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     print(args)
#     files = listdir(args.path, args.a, args.l, args.v)
#     print(next(files))

# 5
# import stat
# import argparse
# from pathlib import Path
# from datetime import datetime
#
# parser = argparse.ArgumentParser(prog='ls',description='show file information')
# parser.add_argument('path',nargs='?',default='.',help='description')
# parser.add_argument('-a',action='store_true',help='all show')
# parser.add_argument('-l',action='store_true',help='show common file')
# parser.add_argument('-v',action='store_true',help='show detailed information')
#
# def listdir(path, all=False, detail=False, human=False):
#     def _gethuman(size:int):
#         units = ' KMGTP'
#         depth = 0
#         while size >= 1000:
#             size = size // 1000
#             depth += 1
#         return '{}{}'.format(size,units[depth])
#     def _listdir(path, all=False, detail=False, human=False):
#         p = Path(path)
#         print(all)
#         for i in p.iterdir():
#             if not all and i.name.startswith('.'):
#                 continue
#             if not human:
#                 yield (i.name)
#             else:
#                 st = i.stat()
#                 mode = stat.filemode(st.st_mode)
#                 atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
#                 size = str(st.st_size) if not human else _gethuman(st.st_size)
#                 yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
#     yield from sorted(_listdir(path, all, detail, human),key=lambda x:x[-1])
#
#
#
#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     print(args)
#     files = listdir(args.path, args.a, args.l, args.v)
#     print(list(files))



import stat
import argparse
from datetime import datetime
from pathlib import  Path

parser = argparse.ArgumentParser(prog='ls',description='show file',add_help=True)
parser.add_argument('path',nargs='?',default='.',help='description')
parser.add_argument('-a',action='store_true',help='show all file')
parser.add_argument('-l',action='store_true',help='show common file')
parser.add_argument('-v',action='store_true',help='show detailed information')

def listdir(path,all=False,detail=False,human=False):
    def _gethuman(size:int):
        units = ' KMGTP'
        depth = 0
        while size >= 1000:
            size = size // 1000
            depth += 1
        return '{}{}'.format(size,units[depth])
    def _listdir(path,all=False,detail=False,human=False):
        p = Path(path)
        for i in p.iterdir():
            if not all and i.name.startswith('.'):
                continue
            if not human:
                yield (i.name,)
            else:
                st = i.stat()
                mode = stat.filemode(st.st_mode)
                atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                size = str(st.st_size) if not human else _gethuman(st.st_size)
                yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
    yield from sorted(_listdir(path, all, detail, human),key=lambda x:x[-1])


if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    parser.print_help()
    files = listdir(args.path, args.a, args.l, args.v)
    print(next(files))