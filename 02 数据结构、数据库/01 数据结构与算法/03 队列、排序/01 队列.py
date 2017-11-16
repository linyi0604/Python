class Queue(object):
    # 创建一个空列表
    def __init__(self):
        self.data = []
    #向队列里添加一个元素
    def enqueue(self ,item):
        self.data.insert(0 , item)
    #删除一个元素
    def dequeue(self):
        return self.data.pop()
    def is_empty(self):
        return self.data==[]
    #返回队列长度
    def size(self):
        return len(self.data)


if __name__=="__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(4)
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())