# import pickle
#
# filename = '/tmp/test20200630'
#
# d = {'a':1,'b':'abc','c':[1,2,3]}
# l = list('123')
# i = 99
#
# with open(filename, 'wb') as f:
#     pickle.dump(d, f)
#     pickle.dump(l,f)
#     pickle.dump(i,f)
#
# with open(filename, 'rb') as f:
#     print(f.read(),f.seek(0))
#     for _ in range(3):
#         x = pickle.load(f)
#         print(type(x),x)
# ==============================================
# import pickle
#
# class AA:
#     tttt = 'ABC'
#     def show(self):
#         print('abc')
#
# a1 = AA()
#
# sr = pickle.dumps(a1)
# print('sr={}'.format(sr))
#
# a2 = pickle.loads(sr)
# print(1, a2)
# print(a2.tttt)
# a2.show()
# ==============================================
import pickle

class AAA:
    def __init__(self):
        self.tttt = 'abc'

a1 = AAA()

ser = pickle.dumps(a1)
print('ser={}'.format(ser))

a2 = pickle.loads(ser)
print(a2, type(a2))
print(a2.tttt)
print(id(a1), id(a2))