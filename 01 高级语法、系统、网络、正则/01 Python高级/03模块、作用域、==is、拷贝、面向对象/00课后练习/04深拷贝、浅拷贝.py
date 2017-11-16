'''
浅拷贝： obj2 = copy.copy(obj1)
    他会对obj1的第一层对象的引用拷贝给obj2
深拷贝： obj2 = copy.deepcopy(obj1)
    会对obj1的所有引用的内部的引用一直追寻到对象进行复制一份全新的给obj2
    
    
特殊情况： 如果拷贝对象是 元组 等不可变类型，那么深拷贝和浅拷贝的结果都只返回了相同的引用
'''
list = [1,2,["a","b"]]

list1 = list

import copy
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