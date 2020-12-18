# commands = {}
#
# def reg(name, fn):
#     commands[name] = fn
#
# def defaultfunc():
#     print("Unkown command")
#
# def dispatcher():
#     while True:
#         cmd = input(">>>")
#         if cmd.strip() == 'quit':
#             return
#         commands.get(cmd, defaultfunc)()
#
# def foo1():
#     print('welcome magedu')
#
# def foo2():
#     print('welcome magedu111')
#
# reg('mag', foo1)
# reg('py', foo2)
# dispatcher()
# =============================================================
# def cmds_dispatcher():
#     commands = {}
#
#     def reg(name):
#         def _reg(fn):
#             commands[name] = fn
#             return fn
#         return _reg
#
#     def defaultfunc():
#         print("Unkown command")
#
#     def dispatcher():
#         while True:
#             cmd = input('>>>')
#             if cmd.strip() == 'quit':
#                 return
#             commands.get(cmd, defaultfunc)()
#     return reg, dispatcher
# reg,dis = cmds_dispatcher()
#
# @reg('mag')
# def foo1():
#     print('welcome magedu')
#
# @reg('py')
# def foo2():
#     print('welcome magedu2222')
#
# dis()
# ===========================================================
from functools import partial

def command_dispatcher():
    cmd_tb1 = {}

    def reg(cmd, *args, **kwargs):
        def _reg(fn):
            func = partial(fn, *args, **kwargs)
            cmd_tb1[cmd] = func
            return func
        return _reg

    def default_func():
        print('Unknow command')

    def dispatcher():
        while True:
            cmd = input('Please input cmd >>>')
            if cmd.strip() == '':
                return
            cmd_tb1.get(cmd, default_func)()
    return reg, dispatcher

reg,dispatcher = command_dispatcher()

@reg('mag',z=200, y=300, x=100)
def foo1(x,y,z):
    print('magedu',x,y,z)

@reg('py',300,b=400)
def foo2(a,b=100):
    print('python',a,b)

dispatcher()