'''
生产和生产数据，消费者消费数据
为了平衡两者速度的不平均，需要一个中间队列平衡。
生产者生产数据丢给队列，消费者从队列中取数据
'''
import queue
import threading
import time
class Producer( threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 1000:
                msg = "生产者产品"+str(count)
                print(msg)
                count+=1
            time.sleep(1)

class Customer(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize()>100:
                msg = "消费者"+self.name+"消费了" + q.get()
                print(msg)
            time.sleep(1)




if __name__ == "__main__":
    #开启一个线程消息队列
    q = queue.Queue()
    #生产初始产品进入队列
    for i in range(500):
        msg = "初始产品"+str(i)
        q.put(msg)


    for i in range(2):
        p = Producer()
        p.start()
        time.sleep(0.5)

    for i in range(2):
        c = Customer()
        c.start()
        time.sleep(0.5)


