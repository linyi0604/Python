#coding:utf8
import unittest

def fib(n):
    if n < 0 :
        return None
    elif n== 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)


class UnitTest(unittest.TestCase):
    # 该方法首先执行 方法名固定
    def setUp(self):
        pass
    # 该方法最后执行 固定
    def tearDown(self):
        pass

    # 测试部分 函数名称 必须以test开头
    def test_app_exists(self):
        pass