import math
#判断传入的参数n 是不是素数 是素数返回True 否则返回False
def isSUshu( n ):
    if n < 2 :      #0 和1 不是素数 直接返回False
        return False
    else:
        i =2
        while i <= math.sqrt(n):        #这个地方如果不理解 换成 i< = n-1      这个地方是一个时间的优化
            if n % i == 0 :
                return False
            i += 1
        return True
#得到 小于n的所有素数的生成器
def getSushuList(n):
     i = 2
     while i <= n:
         if isSUshu(i): #这里调用了判断是不是素数方法 如果是 才用yield关键字把他抛出来
             yield i
         i += 1


a = getSushuList(100)
for temp in a:
    print(temp)



