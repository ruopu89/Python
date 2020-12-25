# class MyIterable:
#     def __str__(self):
#         return "我还不是一个可迭代对象"
#
# mi = MyIterable()
# print(mi)
# ==================================================
# class MyIterable:
#     def __iter__(self):
#         print('iter~~~~~~~')
#         return iter('iter')
#
# mi = MyIterable()
# print(mi)
#
# for i in mi:
#     print(i)
# =========================================================
# g1 = (i for i in range(5)) # 生成器表达式
# print(g1) # 生成器对象
# print(next(g1))
# print(next(g1))
# print('=' * 30)
#
#
# def counter(): # 生成器函数
#     for i in range(5, 10): # 可以使用yield from
#         yield i
#
# g2 = counter() # 生成器函数调用不返回结果，返回一个生成器对象
# print(g2)
# print(next(g2))
# print(next(g2))
# ============================================
a = 'Navigation'
def makekey(s:str):
    # print(3, type(s))
    chars = set(r"""!'"#./\()[],*-""")
    key = s.lower()
    # print(2, key)
    ret = []
    for i,c in enumerate(key):
        if c in chars:
            ret.append(' ')
        else:
            ret.append(c)
    return ''.join(ret).split()

print(makekey(a))