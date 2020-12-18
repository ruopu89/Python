# l1 = list(range(5))
# print(l1)
# # d = dict(l1)
# # TypeError: cannot convert dictionary update sequence element #0 to a sequence
# d = dict(enumerate(l1))
# print(d)
#
# e = enumerate(l1)
# # <enumerate object at 0x7f4a4a51d840>
# # print(e)  # e是一个enumerate对象
# # print(type(e))
# for x in e:
#     print(type(x))

# for i in e:
#     print(i)

# f = dict(e)
# print(f)

# d = {}
# d.setdefault('name', 'Non8e')
# print(d)

# d = dict(a=1, b=2, c='abc')
# for k,v in d.items():
#     print(k)

# while len(d):
#     print(d.popitem())
# keys = []
# for k,v in d.items():
#     if isinstance(k,str):
#         keys.append(k)
# print(keys)
# for k in keys:
#     d.pop(k)
#
# print(d)
# for i in d.keys():
#     d.pop(i)
#     print(d)

import random
d1 = {}
for k in 'abcdef':
    # print('k')
    for i in range(random.randint(1,5)):
        if k not in d1.keys():
            d1[k] = []
            print('!!!!!', type(d1[k]))
        d1[k].append(i)
print(d1)
# d1 = {}
# d1['ab'] = []
# d1[w] = []
# d1['ab'].append('aaa')
# print(d1)
# a = dict()
# # print(type(a))
# a['w'] = []
# print(a,type(a),type(a['w']))
# a['w'].append('abc')
# a['w'].append('bcd')
# print(a)
