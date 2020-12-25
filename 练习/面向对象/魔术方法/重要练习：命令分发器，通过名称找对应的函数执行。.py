# class Dispatcher:
#     def __init__(self):
#         self._run()
#
#     def cmd1(self):
#         print("I'm cmd1")
#
#     def cmd2(self):
#         print("I'm cmd2")
#
#     def _run(self):
#         while True:
#             cmd = input('Plz input a command: ').strip()
#             if cmd == 'quit' or cmd == 'q':
#                 break
#             getattr(self, cmd, lambda: print('Unknown Command {}.'.format(cmd)))()


# 执行Dispatcher类实例化时就可以执行_run方法，之后通过getattr函数来判断用户输入的命令是否在类中有定义，
# getattr()可以通过name返回object的属性值。当属性不存在，将使用default返回，如果没有default，则抛出
# AttributeError。name必须为字符串。这里判断实例中是否有cmd，这个cmd就是while True中定义的用户输入的命
# 令，如果找到，就返回用户输入的方法名的结果。否则返回Unknown Command {cmd}.最后的括号表示找到用户输入的
# 方法名后，要调用这个方法，打印这个方法的执行结果，如cmd1方法的执行结果
# Dispatcher()
# ===========================================================================================
# def dispatcher():
#     cmds = {}
#     def reg(cmd, fn):
#         if isinstance(cmd, str):
#             cmds[cmd] = fn
#         else:
#             print('error')
#
#     def run():
#         while True:
#             cmd = input("plz input command: ")
#             if cmd.strip() == 'quit':
#                 return
#             cmds.get(cmd.strip(), defaultfn)()
#             print(cmds)
#
#     def defaultfn():
#         pass
#
#     return reg,run
#
# reg,run = dispatcher()
# reg('cmd1', lambda :1)
# reg('cmd2', lambda :2)
#
# run()
# =============================
# 把上面的分发器函数改成类
class dispatcher():
    def cmd1(self):
        print('cmd1')

    def reg(self, cmd, fn):
        if isinstance(cmd, str):
            setattr(type(self), cmd, fn)
        else:
            print('error')

    def run(self):
        while True:
            cmd = input("plz input command : ")
            if cmd.strip() == 'quit':
                return
            getattr(self, cmd.strip(), self.defaultfn)()

    def defaultfn(self):
        print('default')

dis = dispatcher()

dis.reg('cmd2', lambda self:print(2))
dis.reg('cmd3', lambda self:print(3))

dis.run()