# 实现单向链表没有实现的`pop`、`remove`、`insert`方法
class SingleNode:
    """代表一个节点，存储节点Node"""
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val)

    __str__ = __repr__

class LinkedList:
    """容器类，按某种方式存储一个个节点"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,val):
        node = SingleNode(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        return self

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next

    def pop(self):
        if self.tail is None:
            raise Exception('Empty')
        tail = self.tail
        prev = tail.prev

        if prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = prev
            prev.next = None
        return tail.val

    def getitem(self,index):
        if index < 0:
            return None
        current = None
        for i,node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is not None:
            return current

    def insert(self, index, val):
        if index < 0:
            raise Exception('Error')

        current = None
        for i,node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:
            self.append(val)
            return

        prev = current.prev
        next = current.next

        node = SingleNode(val)
        if prev is None:
            self.head = node
            node.next = current
            current.prev = node
        else:
            node.prev = prev
            node.next = current
            current.prev = node

ll = LinkedList()
node = SingleNode('abc')
ll.append(node)
node = SingleNode(1)
ll.append(node)
node = SingleNode(2)
ll.append(node)
node = SingleNode(3)
ll.append(node)
node = SingleNode(4)
ll.append(node)
node = SingleNode(5)
ll.append(node)
node = SingleNode(6)
ll.append(node)
node = SingleNode('def')
ll.append(node)

ll.insert(6, 6)
ll.insert(7, 7)
ll.insert(0, '123')
ll.insert(1, '456')  # 在中间插入是无效的，但与pop方法结合时又是起作用的。
ll.insert(30, 'abcdefg')
print(ll)

ll.pop()
ll.pop()
ll.pop()
for node in ll.iternodes(True):
    print(node)