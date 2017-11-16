class Node(object):
    def __init__(self , item ):
        self.item = item
        self.next = None


class LinkStack(object):
    def __init__(self):
        self.top = None
    #判断栈是否为空
    def is_empty(self):
        return self.top is None
    #添加一个新的元素item到栈顶
    def push(self,item):
        node = Node(item)
        if self.is_empty():
            self.top = node
        else :
            node.next= self.top
            self.top = node
    #弹出栈顶元素
    def pop(self):
        if self.is_empty():
            return None
        else:
            res = self.peek()
            self.top = self.top.next
            return res
    #返回栈顶元素
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.item

    #返回栈的元素个数
    def size(self):
        if self.is_empty():
            return 0
        else:
            cur = self.top
            count = 1
            while cur.next is not None:
                count +=1
                cur = cur.next
            return count




if __name__ == "__main__":

    ls = LinkStack()
    print(ls.peek())
    print(ls.pop())
    print(ls.is_empty())
    print(ls.size())
    ls.push(1)
    print(ls.size())
    print(ls.is_empty())
    print(ls.peek())
    print(ls.pop())
    print(ls.is_empty())

