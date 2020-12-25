# # 同学实现
# """节点类"""
# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
#
#     def __repr__(self):
#         return repr(self.data)
#
# """容器"""
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     """获取长度"""
#     def __len__(self):
#         prev = self.head
#         length = 0
#         while prev:
#             length += 1
#             prev = prev.next
#         return length
#
#     """追加节点"""
#     def append(self, item):
#         node = Node(item)
#         if self.head is None:
#             self.head = node
#         else:
#             self.tail.next = node
#             node.prev = self.tail
#         self.tail = node
#
#     """获取节点"""
#     def __getitem__(self, index):
#         index = index if index >= 0 else len(self) + index  # 支持负索引
#         if len(self) < index:  # 超界返回None
#             return None
#         prev = self.head
#         while index:
#             prev = prev.next
#             index -= 1
#         return prev
#
#     """插入节点"""
#     def insert(self, index, data):
#         """
#         1. index 插入节点位置包括正负数
#         2. 找到index-1 --> prev_node的节点
#         3. prev_node.next --> node
#            node.next --> prev_node.next.next
#         4. head
#         :param index
#         :param data
#         :return:
#         """
#         node = Node(data)
#         if abs(index + 1) > len(self):
#             return False
#         index = index if index >= 0 else len(self) + index + 1
#         if index == 0:
#             node.nex = self.head
#             self.head = node
#         else:
#             pre = self.__getitem__(index - 1)
#             if pre:
#                 nex = pre.nex
#                 pre.nex = node
#                 node.nex = nex
#             else:
#                 return False
#         return node
#
#     """修改节点"""
#     def __setitem__(self, key, value):
#         node = self.__getitem__(key)
#         if node:
#             node.data = value
#         return node
#
#     """迭代节点"""
#     def __iter__(self):
#         return iter(self.__iternodes())
#
#     def __iternodes(self, reverse=False):
#         current = self.tail if reverse else self.head
#         while current:
#             yield current
#             current = current.prev if reverse else current.next
#
#     """迭代节点"""
#     def show(self):
#         for i in ll.__iternodes():
#             print(i)
#
#     """反转节点"""
#     def reversed(self):
#         for i in ll.__iternodes(reverse=True):
#             print(i)
#
#     """删除某个元素"""
#     def __delete__(self, index):
#         f = index if index > 0 else abs(index + 1)
#         if len(self) <= f:
#             return False
#         prev = self.head
#         index = index if index >= 0 else len(self) + index
#         prep = None
#         while index:
#             prep = prev
#             prev = prev.next
#             index -= 1
#         if not prep:
#             self.head = prev.next
#         else:
#             prep.next = prev.next
#         return prev.data
#
# ll = LinkedList()
# ll.append(1)
# ll.append(11)
# ll.append(111)
# ll.append(1111)
# ll.append(11111)
# ll.show()
# ll.reversed()
# =========================================================================
# 老师实现
class SingleNode:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.item)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0   # 增加或减少时就开始计数

    def __len__(self):
        return self.size

    def append(self, item):
        node = SingleNode(item)  # 追加
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

        self.size += 1

    def insert(self, index, item):
        if index < 0:
            raise  ValueError('Wrong Index {}'.format(index))
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
# 没找到索引，就是超界了，可以直接抛出异常，也可以转成尾部追加
        if current is None:
            self.append(item)  # 链表为空也可以加入
            return
        # 找到了
        node = SingleNode(item)
        prev = current.prev

        if prev is None:  # head node
            self.head = node
        else:
            prev.next = node
            node.prev = prev

        node.next = current
        current.prev = node

        self.size += 1

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

        self.size -= 1
        return item

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')
        if index < 0:
            raise ValueError('Wrong Index {}'.format(index))

        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:  # Not Found
            raise ValueError('Wrong Index {} out of boundary'.format(index))

        prev = current.prev
        next = current.next

        if prev is None and next is None:  # only one node
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
        self.size -= 1

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next

    __iter__ = iternodes

    def __setitem__(self, key, value):
        self[key].item = value

    def __getitem__(self, index):
        for i,node in enumerate(self.iternodes(False if index >= 0 else True), 0 if index >= 0 else 1):
            if i == abs(index):
                return node

abc = LinkedList()
abc.append(123)
abc.append(234)
abc.append(345)

