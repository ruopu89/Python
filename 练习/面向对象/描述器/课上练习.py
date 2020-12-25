# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#
# print('-' * 20)
# print(B.x.a1)
# print('=' * 20)
# b = B()
# print(b.x.a1)
# =================================
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self, instance, owner):
#         print("A.__get__ {} {} {}".format(self, instance, owner))
#         return self
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#
# print('-' * 20)
# # 输出：
# # A.init
# # --------------------
# # 类加载的时候，类变量需要先生成，而类B的x属性是类A的实例，所以类A先初始化，所以打印A.init。
# print(B.x)
# # # print(B.x.a1)
# print('=' * 20)
# b = B()
# print(b.x)
# print(b.x.a1)
# ============================================================================
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     def __get__(self, instance, owner):
#         print("A.__get__ {} {} {}".format(self, instance, owner))
#         return self
#
#     def __set__(self, instance, value):
#         print('A.__set__ {} {} {}'.format(self, instance, value))
#         self.data = value
#
# class B:
#     x = A()
#     def __init__(self):
#         print('B.init')
#         # self.b = A()
#         self.x = 'b.x'
#         self.y = 'b.y'
#
# # print('-' * 20)
# # print(B.x)
# # print(B.x.a1)
# print('=' * 20)
# b = B()
# print(b.x.a1)
# print(b.y)
# print('字典')
# print(b.__dict__)
# print(B.__dict__)
# print(b.x.a1)
# print(b.b)
# b.x = 500
# B.x = 600
# =========================================
class A:
    def __init__(self):
        print('A.init')
        self.a1 = 'a1'

    def __get__(self, instance, owner):
        print('A.__get__', self, instance, owner)
        return self  # 这里返回self，下面就可以使用b.x.a1了


# 加入__get__方法，再调用A类时，就会被这个方法拦截

class B:
    x = A()  # B类被扫描完就会生成A实例

    def __init__(self):
        print('B.init')
        self.x = 100
        # self.x = A()

print(B.x.a1)
b = B()
print(b.x)