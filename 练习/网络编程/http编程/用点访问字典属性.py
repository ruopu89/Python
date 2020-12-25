# class MyDict(dict):
#     def __getattr__(self, item):
#         return self[item]
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#
# test = MyDict()
# test.update(x=1)
# print(test.x)

# class dotdict(dict):
#     __getattr__ = dict.get
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__
#
# mydict = {'val': 'it works'}
# nested_dict = {'val':'nested works too'}
# mydict = dotdict(mydict)
# print(mydict.val)
#
# mydict.nested = dotdict(nested_dict)
# print(mydict.nested.val)

class MyDict(dict):
    def __init__(self, **kwargs):
        super(MyDict, self).__init__(kwargs)
        self.__dict__ = self

if __name__ == '__main__':
    a = MyDict(x=1, y=2, z=3)
    print(a)
    print(a.x, a.z)