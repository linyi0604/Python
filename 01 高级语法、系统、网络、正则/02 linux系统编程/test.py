'''
进程线程
'''
import time
import multiprocessing
import random
def demo(i):
    print(i,"开始")
    time.sleep(random.random())
    print(i, "结束")



if __name__ =="__main__":
    pool = multiprocessing.Pool(5)
    for i in range(20):
        pool.apply( func=demo ,args=(i,)  )

    pool.close()
    pool.join()

