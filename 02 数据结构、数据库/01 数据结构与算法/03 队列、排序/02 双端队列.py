class Deque(object):
    # 创建一个空队列
    def __init__(self):
        self.data = []
    #头部添加数据
    def add_front(self , item):
        self.data.insert(0 , item)
    #尾部添加数据
    def add_rear(self,item):
        self.data.append(item)
    #头部删除数据
    def remove_front(self):
        return self.data.pop(0)
    #从尾部删除元素
    def remove_rear(self):
        return self.data.pop()
    #判断是否为空
    def is_empty(self):
        return self.data == []
    #大小
    def size(self):
        return len(self.data)



if __name__ == "__main__":
    dq = Deque()
    dq.add_front(1)
    dq.add_rear(2)
    print(dq.remove_front())
    print(dq.remove_rear())