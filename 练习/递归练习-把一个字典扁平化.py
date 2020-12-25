# source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
# target = {}
#
# def flatmap(src=dict,prefix=''):
#     for k,v in src.items():
#         if isinstance(v,(list,tuple,set,dict)):
#             flatmap(v,prefix=prefix+k+'.')
#         else:
#             target[prefix+k] = v
#
# flatmap(source)
# print(target)
# ======================================================
# source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':6}}}
#
# def flatmap(src,dest=None,prefix=''):
#     if dest == None:
#         dest = {}
#     for k,v in src.items():
#         if isinstance(v,(list,tuple,set,dict)):
#             flatmap(v,dest,prefix=prefix+k+'.')
#         else:
#             dest[prefix+k] = v
#     return dest
#
# print(flatmap(source))
# ========================================================
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':6}}}

def flatmap(src):
    def _flatmap(src,dest=None,prefix=''):
        for k,v in src.items():
            key = prefix+k
            if isinstance(v,(list,tuple,set,dict)):
                _flatmap(v,dest,key+'.')
            else:
                dest[key] = v

    dest = {}
    _flatmap(src,dest)
    return dest

print(flatmap(source))