# 单向链表1
# 对于链表来说，每一个结点是一个独立的对象，结点自己知道内容是什么，下一跳是什么。而链表则是一个容器，它内部装着一个个结点对象。所以，建议设计2个类，一个结点Node类，一个链表LinkedList类。
# 将链表的整体看作一个对象，是一个容器，容器中间放的是相同的，只是实例不同而已。实例有两个属性，一个是插入的内容，一个是内容指向
# 方法1
#
# class SingleNode:
#     """代表一个节点，存储节点Node"""
#     def __init__(self, val, nextX=None):
#         self.val = val
#         self.nextX = nextX
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
#     def append(self, val):
#         node = SingleNode(val)
#         prev = self.tail
#         if prev is None:
#             self.head = node
#         else:
#             prev.next = node
#         self.nodes.append(node)
#         self.tail = node
#
#     def __getitem__(self, item):
#         return self.nodes[item]
#     #
#     # def __len__(self):
#     #     return len(self.nodes)
#     #
#     # def iternodes(selfself, reverse=False):
#     #     current = self.head
#     #     while current:
#     #         yield current
#     #     current = current.next
#
#     # def __str__(self):
#     #     return str(self.val)
#     #
#     # __repr__ = __str__
#
# a = LinkedList()
# a.append(3)
# # print(dir(a))
# print(a[0])
# ===================================================================================
# 方法2
# class SingleNode:
#     def __init__(self, val, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
#
#     def __repr__(self):
#         return str(self.val)
#
#     __str__ = __repr__
#
# class LinkedList:
#     def __init__(self):
#         self.nodes = []
#         self.head = None
#         self.tail = None
#
#     def __len__(self):
#         return len(self.nodes)
#
#     def append(self, val):
#         node = SingleNode(val)
#         prev = self.tail
#         if prev is None:
#             self.head = node
#         else:
#             prev.next = node
#         self.nodes.append(node)
#         self.tail = node
#
#     def iternodes(self, reverse=False):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#
#     def __getitem__(self, item):
#         return self.nodes[item]
#
# ll = LinkedList()
# node = SingleNode(5)
# ll.append(node)
# node = SingleNode(8)
# ll.append(node)
#
# print(ll)
# for node in ll.iternodes():
#     print(node)
#
# print(ll[1])
# ==================================================================
# 方法3
# class SingleNode:
#     def __init__(self, item, next=None):
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
#     def append(self, item):
#         node = SingleNode(item)
#         if self.head is None:
#             self.head = node
#         else:
#             self.tail.next = node
#         self.tail = node
#         return self
#
#     def iternodes(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#
#
# ll = LinkedList()
# ll.append('abc')
# ll.append(1).append(2)
# ll.append('def')
#
# print(ll.head, ll.tail)
#
# for item in ll.iternodes():
#     print(item)
# ====================================================
# 借助列表实现，这和上面的方法差不多，是PDF中记录的方法
# class SingleNode:
#     def __init__(self, item, next=None):
#         self.item = item
#         self.nexta = next
#
#     def __repr__(self):
#         return repr(self.item)
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.items = []
#
#     def append(self, item):
#         node = SingleNode(item)
#         # print(node.__dict__,'0000000000000')
#         # print(self.head.__dict__, 1)
#         # print(self.tail.__dict__, 2)
#         if self.head is None:
#             self.head = node
#             # print(self.head.__dict__, 3)
#
#         else:
#             self.tail.nexta = node
#             # print(self.tail.__dict__, 4)
#             # print(self.head.__dict__, 2)
#             # print(self.__dict__, 3)
#             # print(self.__dict__, '***', dir(self))
#         self.tail = node
#         # print(self.tail.__dict__, 5)
#
#         self.items.append(node)
#         return self
#
#     def iternodes(self):
#         current = self.head
#         # print(current)
#         # print(dir(self.head))
#         # yield current
#         while current:
#             print(current, 1)
#             # print(dir(current))
#             yield current
#             # next current
#             # yield self.head
#             current = current.nexta
#             # self.head = self.head.nexta
#
#     # def getitem(self, index):
#     #     return self.items[index]
#
# ll = LinkedList()
# ll.append('abc')
# ll.append(1).append(2)
# ll.append('def')
#
# # print(ll.head, ll.tail)
#
# for item in ll.iternodes():
#     print(item)

# for i in range(len(ll.items)):
#     print(ll.getitem(i))
# print(ll.__dict__)
# print(LinkedList.__dict__)
# print(ll.tail)
# print(dir(ll))

# test = SingleNode(111)
# print(test)
# print(test.__dict__)
# =======================================================================================
# 双向链表
# 实现单向链表没有实现的pop、remove、insert方法
# class SingleNode:
#     """代表一个节点，存储节点Node"""
#     def __init__(self, val, next=None, prev=None):
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
#         self.head = None
#         self.tail = None
#
#     # def append(self, val):
#     #     node = SingleNode(val)
#     #     if self.head is None:
#     #         self.head = node
#     #     else:
#     #         self.tail.next = node
#     #         node.prev = self.tail
#     #     self.tail = node
#
#     def iternodes(self, reverse=False):
#         current = self.tail if reverse else self.head
#         while current:
#             yield current
#             current = current.prev if reverse else current.next
#
#     def pop(self):
#         if self.tail is None:
#             raise Exception('Empty')
#         tail = self.tail
#         prev = tail.prev
#         if prev is None:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = prev
#             prev.next = None
#         return tail.val
#
#     def getitem(self, index):
#         if index < 0:
#             return None
#         current = None
#         for i,node in enumerate(self.iternodes()):
#             if i == index:
#                 current = node
#                 break
#         if current is not None:
#             return current
#
#     def insert(self, index, val):
#         if index < 0:
#             raise Exception('Error')
#
#         current = None
#         for i,node in enumerate(self.iternodes()):
#             if i == index:
#                 current = node
#                 break
#         if current is None:
#             self.append(val)
#             return
#
#         prev = current.prev
#         next = current.next
#
#         node = SingleNode(val)
#         if prev is None:
#             self.head = node
#             node.next = current
#             current.prev = node
#         else:
#             node.prev = prev
#             node.next = current
#             current.prev = node
#
# ll = LinkedList()
# node = SingleNode('abc')
# ll.append(node)
# node = SingleNode(1)
# ll.append(node)
# node = SingleNode(2)
# ll.append(node)
# node = SingleNode(3)
# ll.append(node)
# node = SingleNode(4)
# ll.append(node)
# node = SingleNode(5)
# ll.append(node)
# node = SingleNode(6)
# ll.append(node)
# node = SingleNode('def')
# ll.append(node)
# ll.append(987654321)

# for i,node in enumerate(ll.iternodes()):
#     print(i,node)

# ll.insert(6, 60)
# ll.insert(7, 70)
# ll.insert(0, '123')
# ll.insert(2, '4568888888888')
# ll.insert(30, 'abcdefg')

# ll.pop()
# ll.pop()
# ll.pop()
# for i,node in enumerate(ll.iternodes()):
#     print(i,node)
# =============================================================
# 双向链表实现方法2
class SingleNode:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "({} <== {} ==> {})".format(self.prev.item if self.prev else None, self.item, self.next.item if self.next else None)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        return self

    def insert(self, index, item):
        if index < 0:
            raise IndexError('Not negative index {}'.format(index))

        current = None
        for i,node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:
            self.append(item)
            return
        node = SingleNode(item)
        prev = current.prev
        next = current
        if prev is None:
            self.head = node
        else:
            prev.next = node
            node.prev = prev
        node.next = next
        next.prev = node

    def pop(self):
        if self.tail is None:
            raise Exception('Empty')
        node = self.tail
        item = node.item
        prev = node.prev
        if prev is None:
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev
        return item

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')

        if index < 0:
            raise IndexError('Not negative index {}'.format(index))

        current = None
        for i,node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:
            raise IndexError('Wrong index {}'.format(index))

        prev = current.prev
        next = current.next

        if prev is None and next is None:
            self.head = None
            self.tail = None
        elif prev is None:
            self.head = next
            next.prev = None
        elif next is None:
            self.tail = prev
            prev.next = None
        else:
            prev.next = next
            next.prev = prev

        del current

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next

ll = LinkedList()
ll.append('abc')
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append('def')
print(ll.head, ll.tail)

for x in ll.iternodes(True):
    print(x)

print('============')

ll.remove(6)
ll.remove(5)
ll.remove(0)
ll.remove(1)

for x in ll.iternodes():
    print(x)

print('~~~~~~~~~~~~~~~~~~')

ll.insert(3, 5)
ll.insert(20, 'def')
ll.insert(1, 2)
ll.insert(0, 'abc')
for x in ll.iternodes():
    print(x)