# from os import path

# p = path.join('/etc','network','interfaces')
# print(type(p),p)
# print(path.exists(p))
# print(path.split(p))
# print(path.abspath('.'))
# print(path.dirname(p))
# print(path.basename(p))
# print(path.splitdrive(p))

# p1 = path.abspath(__file__)
# print(p1,path.basename(p1))
# while p1 == path.dirname(p1):
#     p1 = path.dirname(p1)
#     print(22,p1,path.basename(p1))
#========================================
from pathlib import Path

# p = Path()
# print(type(p))
# p = Path('/etc','network','interfaces')
# print(p)
# p.absolute()
# print(p)
# p = p.joinpath('a','b')
# print(p)
# p /= 'c'
# print(p)
# p1 = Path('/etc')
# p1.absolute()
# # p2 = '/'/'etc' / 'sysconfig'
# p2 = Path('')
# print(p2)
# p2 = p2 / '/etc' / 'sysconfig'
# print(p2)
# print(p2.parts)
# p2.joinpath('a/b','c')
# print(1, p2)
# p2 = p2 / 'a/b' / 'c'
# print(2, p2)
# p2 = p2 / 'etc' / 'sysconfig'
# print(3, p2)
# print(4, str(p2))
# print(p2.parent)
# print(p2.parent.parent)
#
# print(list(p2.parents))
# p2 /= 'a/b/c/d'
# print(list(p2.parents))
# print(next(iter(p2.parents)))

# p = Path('a')
# print(1, p)
# p1 = 'b' / p
# print(2, p1)
# p2 = Path('c')
# print(3, p2)
# p3 = p2 / p1
# print(4, p3)
# # print(p3.parts)
# # print(p3.parent)
#
# for x in p3.parents:
#     print(x)

# p = Path('/magedu/mysqlinstall/mysql.tar.gz')
# print(1, p.name)
# print(2, p.suffix)
# print(3, p.suffixes)
# print(4, p.stem)
# print(5, p.with_name('mysql-5.tgz'))
# p = Path('README.tsst')
# print(p.with_suffix('.txt1'))

# p = Path('/home/shouyu')
# p /= 'a/b/c/d'
# p.exists()

# p.mkdir(parents=True)
# p.mkdir(parents=True,exist_ok=True)
# p /= 'readme.txt'
# print(p)
# print(p.rmdir())
# p.parent.rmdir()
# p.parent.exists()
# p.mkdir()
# p.mkdir(parents=True)
# for x in p.parents[len(p.parents)-1].iterdir():
#     print('s', x,end='\t')
#     if x.is_dir():
#         flag = False
#         for _ in x.iterdir():
#             flag = True
#             break
#         print('dir','Not Empty' if flag else 'Empty', sep='\t')
#     elif x.is_file():
#         print('file')
#     else:
#         print('other file')
# print(p.parents[0], p.parents[1], p.parents[2])
# p = Path('a/b/c/d')
# # print(p.parent.parent)
# for x in p.parents:
#     continue
# =============================================
f = [PosixPath('/home/ubuntu/.bash_logout'), PosixPath('/home/ubuntu/.profile'), PosixPath('/home/ubuntu/.python_history'), PosixPath('/home/ubuntu/.sudo_as_admin_successful'), PosixPath('/home/ubuntu/.viminfo'), PosixPath('/home/ubuntu/.bashrc'), PosixPath('/home/ubuntu/.bash_history')]
t = '/home/ubuntu/.bash_logout'
print(t)