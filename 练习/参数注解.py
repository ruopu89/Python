# signature(callable)，获取签名（函数签名包含了一个函数的信息，包括函数名、它的参数类型、它所在的类和名称空间及其他信息）
# import inspect
#
# def add(x:int=2, y:int=3, *args, **kwargs) -> int:
#     return x + y
#
# print(1, add.__annotations__)
# sig = inspect.signature(add)
# print(2, sig,'~~~~~~~', type(sig))
# print(3, 'params: ',sig.parameters)
# print(4, 'return: ', sig.return_annotation)
# print(5, sig.parameters['args'])
# print(6, sig.parameters['args'].annotation)
# print(7, sig.parameters['x'].annotation)
# print(8, sig.parameters['kwargs'].annotation)
# ===============================================================
# import inspect
# def add(x, y:int=7, *args, z, t=10, **kwargs) -> int:
#     return x + y
#
# sig = inspect.signature(add)
# print(1, sig)
# print(2, 'params:', sig.parameters)
# print(3, 'return:', sig.return_annotation)
# print('~~~~~~~~~~~~~~~~~')
# for i, item in enumerate(sig.parameters.items()):
#     name, param = item
#     print(i+1, name, 'annotation:{},kind:{},default:{}'.format(param.annotation, param.kind, param.default))
#     print(param.default is param.empty, end='\n\n')

# add(4)
# add(4,7)
# ===================================================
# 查检实参是否符合要求
# import inspect
#
# def check(fn):
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#
#         values = list(params.values())  # 输出如：[<Parameter "x">, <Parameter "y: int = 7">]
#         print('~~~~~~', values,values[1])
#         for i,p in enumerate(args):
#             param = values[i]  # 这里param得到的值是x或y: int = 7
#             print('!!!!!', param)
#             if param.annotation is not param.empty and not isinstance(p, param.annotation):
#                 print(p, '!==', values[i].annotation)
#         for k,v in kwargs.items():
#             if params[k].annotation is not inspect._empty and not isinstance(v, params[k].annotation):
#                 print(k,v,'!==',params[k].annotation)
#         return fn(*args, **kwargs)
#     return wrapper
#
# @check
# def add(x,y:int=7) -> int:
#     # print(x+y)
#     return x + y
#
# print(add(20,2))
# ============================
# partial方法





