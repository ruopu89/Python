# 用面向对象实现LinkedList链表
# 单向链表实现`append`、`iternodes`方法
# 双向链表实现`append`、`pop`、`insert`、`remove`、`iternodes`方法
# 参考
# 对于链表来说，每一个结点是一个独立的对象，结点自己知道内容是什么，下一跳是什么。而链表则是一个容器，它内部装着一个个结点对象。所以，建议设计2个类，一个结点Node类，一个链表LinkedList类。
# 将链表的整体看作一个对象，是一个容器，容器中间放的是相同的，只是实例不同而已。实例有两个属性，一个是插入的内容，一个是内容指向
# class SingleNode:
#     """代表一个节点，存储节点Node"""
#     def __init__(self,val,next=None):
#         self.val = val
#         self.next = next
#
#     def __str__(self):
#         return str(self.val)
#
#     __repr__ = __str__
#
# class LinkedList:
#     """容器类，按某种方式存储一个个节点"""
#     def __init__(self):
#         self.nodes = []
#         self.head = None
#         self.tail = None
#
#     def append(self,val):
#         node = SingleNode(val)
#         prev = self.tail
#         if prev is None:
#             self.head = node
#         # else:
#         #     prev.next = node
#         self.nodes.append(node)
#         self.tail = node
#
# a = LinkedList()
# a.append(3)
# a.append(34)
# a.append(234)
# print(a)
# print(a.nodes)
# print(a.head,a.tail)
# =========================================================
# class SingleNone:
#     """代表一个节点，存储节点Node"""
#     def __init__(self,val,next=None,prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
#
#     def __repr__(self):
#         return str(self.val)
#
#     def __str__(self):
#         return str(self.val)
#
# class LinkedList:
#     """容器类，按某种方式存储一个个节点"""
#     def __init__(self):
#         self.nodes = []
#         self.head = None
#         self.tail = None
#
#     def __len__(self):
#         return len(self.nodes)
#
#     def append(self,val):
#         node = SingleNone(val)
#         prev = self.head
#         if prev is None:
#             self.head = node
#         else:
#             prev.next = node
#         self.nodes.append(node)
#         self.tail = node
#
#     def iternodes(self,reverse=False):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#             # print(222,current.next)
#
#     def __getitem__(self, item):
#         return self.nodes[item]

# ll = LinkedList()
# node = SingleNone(5)
# ll.append(node)
# node = SingleNone(7)
# ll.append(node)
# node = SingleNone(8)
# ll.append(node)
# node = SingleNone(9)
# ll.append(node)
# print('ll:{}'.format(ll.__dict__))
# print('node:{}'.format(node.__dict__))
# ll.append(5)
# ll.append(4)
# ll.append(3)
# ll.append(2)
# ll.append(1)
# print(ll.__dict__)
# for node in ll.iternodes():
#     print(node)
# =====================================================
# class SingleNode:
#     def __init__(self,item,next=None):
#         self.item = item
#         self.next = next
#
#     def __repr__(self):
#         return repr(self.item)
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self,item):
#         node = SingleNode(item)
#         if self.head is None:
#             self.head = node
#             # print(11111111111111,node)
#         else:
#             self.tail.next = node
#             print(222222222, self.tail.next,self.head.next)
#         self.tail = node
#         # abc = self.head
#         # print(222222222222222,abc,abc.next)
#         # print(3333333333333, self.tail.next)
#         return self
#
#     def iternodes(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#             # print(111111, current)
#
#
# ll = LinkedList()
# ll.append('abc')
# ll.append(1).append(2)
# ll.append('def')
# print(ll.__dict__)
# for item in ll.iternodes():
#     print(item)
# =======================================================
# 借助列表实现
class SingleNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return repr(self.item)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def append(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
            # print(self.head.__dict__, 'a')
        else:
            self.tail.next = node
            print(self.tail.__dict__, id(self.tail.__dict__), 'b')
        self.tail = node
        print(self.tail.__dict__,id(self.tail.__dict__), 'c')
        self.items.append(node)
        return self

    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def getitem(self, index):
        return self.items[index]


ll = LinkedList()
ll.append('abc')
ll.append(1).append(2)
ll.append('def')

# print(ll.head, ll.tail)

for item in ll.iternodes():
    print(item)

# for i in range(len(ll.items)):
#     print(ll.getitem(i))