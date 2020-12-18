# 有一个文件，对其进行单词统计，不区分大小写，并显示单词重复最多的10个单词
# /media/shouyu/C64CC89B4CC8879F/works/马哥2018python/01.课堂笔记/p10c06/sample.txt

# d = {}
# with open('/media/shouyu/C64CC89B4CC8879F/works/马哥2018python/01.课堂笔记/p10c06/sample.txt',encoding='utf8') as f:
#     for line in f:
#         words = line.split()
#         for word in map(str.lower, words):
#             # print(12345, word)
# # word是一个个以空格分隔后的单词或字符
#             d[word] = d.get(word, 0) + 1
#
# print(sorted(d.items(), key=lambda a:a[1], reverse=True))
#
# for k in d.keys():
#     if k.find('path') > -1:
#         print(k)
# ======================================================================
def makekey(s:str):
    print(3, s, type(s))
    chars = set(r"""!'"#./\()[],*-""")
    key = s.lower()
    print(2, key)
    ret = []
    for i,c in enumerate(key):
        if c in chars:
            ret.append(' ')
        else:
            ret.append(c)
    return ''.join(ret).split()

d = {}
with open('/media/shouyu/C64CC89B4CC8879F/works/马哥2018python/01.课堂笔记/p10c06/sample.txt', encoding='utf8') as f:
    for line in f:
        words = line.split()
        # print(1, type(line), type(line.split()))
        for wordlist in map(makekey, words):
            for word in wordlist:
                d[word] = d.get(word, 0) + 1

items = iter(sorted(d.items(), key=lambda item:item[1], reverse=True))
# print(type(iter(items)))
for _ in range(10):
    print(next(items))
# for _ in range(10):
# for k,v in iter(sorted(d.items(), key=lambda item:item[1], reverse=True)):
#     # print(k,v)
#     next(k,v)

    # next(sorted(d.items(), key=lambda item:item[1], reverse=True))

# ===========================================================================
# 分割key的另一种思路
# def makekey(s:str):
#     chars = set(r"""!'"#./\()[],*-""")
#     key = s.lower()
#     ret = []
#     start = 0
#     length = len(key)
#
#     for i,c in enumerate(key):
#         # print('c: {}'.format(c))
#         if c in chars:
#             if start == i:  # 0  0
#                 start += 1  # 1  0
#                 continue
#             ret.append(key[start:i])
#             print('ret: {}'.format(ret))
#             start = i + 1
#     else:
#         if start < len(key):
#             ret.append(key[start:])
#     return ret
#
# print(makekey('os.path.exists(path)'))
# print(makekey('os.path.-exists(path)'))
# print(makekey('path.os...'))
# print(makekey('path'))
# print(makekey('path-p'))
# print(makekey('***...'))
# print(makekey(''))