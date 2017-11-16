'''
Queue 是一个消息队列
q= Queue(n) 初始化最大接收消息的数量，如果没传参或者为负数，则可以无限扩展
q.empty() 检查是否为空    空了True
q.full() 检查是否满了     满了True
Queue.get( block, timeout ) :  把消息从队列当中取出来
        block默认为True，代表阻塞，如果不穿参数默认阻塞读取，
            此时如果队列没有消息，他会一直读取直到读到消息
            如果设置了timeout，会timeout秒后没读到消息抛出Queue.Empty()异常
        block设为False的时候，如果消息队列为空会立即抛出异常
Queue.get_nowait(): 相当于 Queue.get(False)

Queue.put(item,block,timeout): 
    item是写进队列的内容，
    block默认为True代表阻塞，代表如果队列满了，会一直等队列有位置
            如果block为False 队列慢的话会立即抛出异常
    timeout 设置时间，到时间还没有空位写内容就会抛出Queue.Full 异常
Queue.put_nowait() 相当于Queue.put(item , False ) 如果队列满 直接抛出异常
            

'''
from multiprocessing import Queue
q = Queue(3) #初始化一个Queue对象，最多可以接收三条 put消息
q.put("消息1")
q.put("消息2")
print( q.full()) #false
q.put("消息3")
print(q.full()) #True

#消息队列满了之后，再往里put消息会抛出异常

try:
    q.put("消息4", True ,2)   #两秒后抛出异常
except:
    print("消息队列满了，现在有消息%s条"%q.qsize()) #qsize() 获取消息数目

try :
    q.put_nowait("消息4")     #如果满了会立即抛出异常
except:
    print("消息队列满了，现在有消息%s条" % q.qsize())  # qsize() 获取消息数目


#推荐的方式，先判断再写入
if not q.full():
    q.put_nowait("消息4")

#读取的时候先判断
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
        #每get一条，就少一条
        print("现在有消息%s条" % q.qsize())









