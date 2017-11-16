'''

生产者 生产数据
消费者 消费数据

避免生产者与消费者直接进行通信，那样耦合度太大
我们开启一个队列，生产者向里面生产 消费者向从里面拿
这样能有效的控制生产与消费的速度不平衡的问题

'''
import threading
import queue

class Producer(threading.Thread):
    def run(self):
        while True:
            if q.qsize() < 500 :
                for i in range(1000):
                    msg = "生产消息"+str(i)
                    print(msg)
                    q.put(msg)


class Customer(threading.Thread):
    def run(self):
        while True:
            if q.qsize()>= 500:
                for i in range(300):
                    msg = "消费者"+str(i)+"消费"+q.get()
                    print(msg)





if __name__ == "__main__":
    q = queue.Queue()   #获取一个队列 做生产者和消费者的中间件
    for i in range(500):
        q.put("初始产品"+str(i))
    for i in range(2):
        t = Producer()
        t.start()
    for i in range(5):
        t = Customer()
        t.start()


