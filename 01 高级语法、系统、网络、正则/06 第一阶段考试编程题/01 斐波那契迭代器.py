'''
自定义一个迭代器类，用于生成斐波拉契数列，并使用该迭代器计算斐波拉契数列前20项的累和。
斐波那契额数：第一项是0 第二项是1  从第三项开始 每项都是前两项的加和
0 1 1 2 3 5
'''


# 前n项斐波那契数的迭代器类
class FibIterator(object):
    def __init__(self ,n ):
        self.n = n
        self.i = 0
        self.num1 = 0
        self.num2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n :
            self.i += 1
            res = self.num1
            self.num1 , self.num2 = self.num2 , self.num1 + self.num2
            return res
        else :
            raise StopIteration

# 生成一个前20项斐波那契数的迭代器 fib20
fib20 = FibIterator(20)

#求出前20项的累加和num
num = 0
for temp in fib20:
    num += temp

print(num)

