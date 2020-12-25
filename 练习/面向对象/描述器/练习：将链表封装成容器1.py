# 要求：
# 1. 提供`__getitem__`、`__iter__`、`__setitem__`方法
# 2. 使用一个列表，辅助完成上面的方法
# 3. 进阶：不使用列表，完成上面的方法
#
# 进阶题
# 实现类property装饰器，类名称为Property。
# 基本结构如下，是一个数据描述器
# =========================================================================
class SingleNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val)


#    def __str__(self):
#        return str(self.val)  # __repr__和__str__都是为了打印使用

class LinkedList:
    def __init__(self):
        # self.nodes = []   # 创建一个容器，放上面的元素。不能用set，有可能去重，另外set是无序的。对不需要插入的列表来说，
        # 检索方便，所以使用了列表。但是插入、remove不合适
        self.head = None
        self.tail = None
        # 这里没有设计self.size是因为这个数据在多线程的情况下不会太准确
        self.size = 0
        self.items = []  # 我们是希望借助列表的查询能力


    # def __len__(self)


    def append(self, item):
        node = SingleNode(item)  # 当前新增的数字
        if self.head is None:
            # 加第一个元素时才会到这里
            self.head = node  # 如果第一个元素是None，那么就把头设置为node
        else:  # 大于1个元素时进入这里
            self.tail.next = node  # 原来的尾部指向自己
            node.prev = self.tail  # 前一个指向尾部
        # prev属性实际在node实例上，所以要改node实例，而不是self.prev。每次调用append方法时都要用到node实例，所以从第二次进来就要让
        # 实例知道node的前一个数字是谁。
        self.tail = node  # 最后把自己修正成尾部
        self.items.append(node)  # 直接使用列表的append方法
        # return self


    def insert(self, index, item):  # 这只能实现从头或尾追加
        if index < 0:
            raise ValueError('Wrong Index {}'.format(index))
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        # 这里就是要用enumerate函数来确定index及其对应的值，最后赋值给current
        if current is None:
            self.append(item)
            return
        # 这里返回的是None，真正返回的内容已经在append方法中返回了。
        # 什么情况下current会等于None？
        prev = current.prev
        node = SingleNode(val)
        if prev is None:  # 头部插入
            self.head = node  # 这就是在设置插入到头部了
        else:
            prev.next = node
            node.prev = prev

        node.next = current
        current.prev = node

        self.items.insert(index, node)


    def pop(self):  # 从尾部弹出一个
        if self.tail is None:  # 如果尾部是None，就抛异常。 == 0
            raise Exception('Empty')
        node = self.tail
        item = node.item
        prev = node.prev
        if prev is None:  # ==1。判断上面定义的tail和prev是否符合条件
            self.head = None  # 如果前一个是None，就表示头是None，否则前一个应该有值
            self.tail = None  # 头是None，就表示尾也是None。
        # 当符合这个条件时就证明只有最后一个值了。再调用pop方法时头和尾就应该是None了。
        else:  # > 1
            self.tail = prev
            prev.next = None
            # 符合这个条件时，就是大小1个元素的时候，弹出一个元素后，尾部就应该变成尾部的前一个元素，前一个元素的下一个元素（也就是尾部）就应该变成None了，因为被弹出了。
            self.items.pop()  # 默认是-1，从最后一个弹出。元素数量已经在上面判断了
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
            raise ValueError('Wrong Index {}. Out of boundary'.format(index))

        prev = current.prev
        next = current.next

        if prev is None and next is None:  # only on node
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
        self.items.pop(index)

    def iternodes(self, reverse=False):  # 暂时只能实现单向。iter表示生成器
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next


# 下面实现容器
    def __len__(self):
        return len(self.items)


    def __getitem__(self, index):
        return self.items[index]  # node

    def __setitem__(self, index, value):
        node = self[index]
        node.item = value


    def __iter__(self):
        return self.iternodes()

test = LinkedList()
print(test.__dict__)
test.append(123)
print(test.append(233))
print(test.__dict__)
print(test.items)