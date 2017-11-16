#coding:utf8
''''''
'''
对于常驻内存的小整数池，深浅拷贝实际上都相当于是浅拷贝 都引用同一份变量

对于一些容器变量：

浅拷贝： objc=copy.copy(obj)  把obj的当前层次所有引用拷贝给objc 

深拷贝： objc = copy.deepcopy(obj) 把obj的所有变量引用追到源头 开辟新的内存 把值存过来
        形成为安全新的另一份数据
     

'''
import copy

a = 1
b = copy.copy(a)
c = copy.deepcopy(a)
print(a is b)   #True
print( a is c)  #True

print("-"*50)

list = [1,2,["a","b"]]

list1 = list
list2 = copy.copy(list)
list3 = copy.deepcopy(list)

list1.append(4)
list[2].append("c")

print(list)
print(list1)    #list1 是list相同引用 两个完全相同
print(list2)    #浅拷贝拷贝当前第一层的所有引用，拷贝了1 2 和内列表的引用，添加元素的时候它获取不到
                #   内列表的引用添加进来了，所以内列表的更改是能看见的
print(list3)    #深拷贝 不会任何更改 完全全新的

'''
特殊情况： 如果拷贝对象是 元组 等不可变类型，那么深拷贝和浅拷贝的结果都只返回了相同的引用
'''
a = (1,2,3)
b  = copy.deepcopy(a)
c = copy.copy(a)
print( b is c )