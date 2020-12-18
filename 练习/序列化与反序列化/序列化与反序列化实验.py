# import pickle
#
# class AAA:
#     def __init__(self):
#         self.tttt = 'abc'
#
# aaa = AAA()
# sr = pickle.dumps(aaa)
# print(len(sr),sr)
#
# file = '/tmp/ser'
# with open(file,'wb') as f:
#     pickle.dump(aaa,f)
# ============================================
# import pickle
#
# with open('/tmp/ser','rb') as f:
#     a = pickle.load(f)
# ========================================
# import pickle
#
# class AAA:
#     def show(self):
#         print('xyz')
#
# with open('/tmp/ser','rb') as f:
#     a = pickle.load(f)
#     print(a)
#     a.show()
# =============================================
# json 测试
# import json
# d = {'name':'Tom','age':20,'interest':['music','movie']}
# j = json.dumps(d)
# print(j)
#
# d1 = json.loads(j)
# print(d1)
# =============================================
# MessagePack测试
import msgpack
import json

d = {'person':[{'name':'tom','age':18},{'name':'jerry','age':16}],'total':2}

j = json.dumps(d)
m = msgpack.dumps(d)

print("json = {}, msgpack = {}".format(len(j), len(m)))
print(j.encode(), len(j.encode()))
print(m, len(m))

u = msgpack.unpackb(m)
print(type(u),u)

u = msgpack.unpackb(m,encoding='utf8')
print(type(u),u)