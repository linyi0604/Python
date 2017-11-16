class Stack(object):
    def __init__(self):
        self.data = []
    #添加元素
    def push(self,item):
        self.data.append(item)
    #弹出元素
    def pop(self):
        return self.data.pop()
    #返回栈顶元素
    def peek(self):
        return self.data[len(self.data) -1 ]
    #判断空
    def is_empty(self):
        if self.data == []:
            return True
        else :
            return False
    #返回元素个数
    def size(self):
        return len(self.data)

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(5)
    print(stack.is_empty())
    print(stack.peek())
    print(stack.size())
    print(stack.pop())
    print(stack.is_empty())

