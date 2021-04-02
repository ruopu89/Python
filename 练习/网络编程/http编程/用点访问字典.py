# 方法一
# class MyDict(dict):
#     def __init__(self, **kwargs):
#         super(MyDict, self).__init__(kwargs)
#         self.__dict__ = self

# if __name__ == '__main__':
#     a = MyDict(x=1, y=2, z=3)
#     print(a)
#     print(a.x)
#     print(a.y)
# =====================================================
# 方法二
# class MyDict(dict):
#     def __getattr__(self, item):
#         return self[item]

#     def __setattr__(self, key, value):
#         self[key] = value

# test = MyDict()
# test.update(x=1)
# print(test.x)
# ==============================================
# 方法三
# class dotdict(dict):
#     __getattr__ = dict.get
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__

# mydict = {'val':'it works'}
# nested_dict = {'val':'nested works too'}
# mydict = dotdict(mydict)
# print(mydict.val)

# mydict.nested = dotdict(nested_dict)
# print(mydict.nested.val)
#=========================================================
def jsonify(kwargs):
    context = kwargs
    print(context)

# jsonify({"a":3})  # def jsonify(kwargs): # 当只接受 kwargs 一个传参时，要传入字典才可以
# jsonify(a=3,b=4) # def jsonify(**kwargs): # 如果形参设置成接受多个参数，可以这样传参
# jsonify(a=3) # def jsonify(kwargs): 定义成这样时，这样传参是不可以的，因为 jsonify 函数中并没有 a 这个关键字参数


# EIP公网带宽
# 100Mbps    118435.2元
# 200Mbps    241075.2元
# 500Mbps    608995.2元