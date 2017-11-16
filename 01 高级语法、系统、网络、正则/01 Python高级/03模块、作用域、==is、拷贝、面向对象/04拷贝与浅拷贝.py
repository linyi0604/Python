'''
浅拷贝： res = copy.copy( obj)
        会把第一层的所有引用拷贝给res
深拷贝:  res = copy.deepcopy( obj )
        是一个递归过程，会把所有引用指向的确实对象复制一份新的给res

例外：当拷贝文件是 不可变类型的时候， 不论深拷贝还是浅拷贝，都只会指向相同文件，
    因为python认为不可变类型，是不会随意发生改变值的
'''
import copy

list1 = [1,2,["a","b"]]
#引用的传递，实际两个变量名指向同一个对象实体
list2 = list1

#浅拷贝 实质是拷贝了第一层所有元素的引用在自己手里，如果元素发生改变，拷贝也会看见
list3  = copy.copy( list1 )
#深拷贝 是指是把所有引用的对象实体拷贝一份形成全新的给自己， 如果源内容改变，拷贝不会发生改变
list4 = copy.deepcopy( list1 )
print("改变之前："+"-"*50)
print(list1)
print(list2)
print(list3)
print(list4)

'''
在list1后面追加元素:
    list1和list2都会发生改变 他们都是指向了同一个对象实体
    list3中 内部列表会改变，因为 浅拷贝文件 存了内列表的引用。但是3不会追加，因为 只拷贝了1 2 和内部列表的引用
    list4 中 不会有任何变化 list4 是深拷贝 完全新的另一个东西
'''


print("追加一个元素3："+"-"*50)
list1.append(3)
print(list1)
print(list2)
print(list3)
print(list4)
print("内部列表增加了元素c："+"-"*50)
list1[2].append("c")
'''
list1 和list2 是同一个对象的引用，都会发生变化
list3 浅拷贝了 1 2 和内列表的引用，所以内列表发生改变 在list3中能体现
list4 是完全了另一个东西 不受任何影响
'''
print(list1)
print(list2)
print(list3)
print(list4)


print("-"*70)

'''
当拷贝文件是 不可变类型的时候， 不论深拷贝还是浅拷贝，都只会指向相同文件，
    因为python认为不可变类型，是不会随意发生改变值的
'''
tu1=(1,2,3)
tu2=copy.copy(tu1)
tu3=copy.deepcopy(tu2)
print(tu2 is tu3)   #true 因为 tu1是不可变类型

'''
拷贝的其他使用方法
'''
#使用字符串的切片
print("使用字符串的切片:")
a="hahha"
b=a[:]
print(b is a)
#字典的拷贝方法
print("字典的拷贝方法:")
dic={"name":"zhangsan"}
dic2=dic.copy()
print(dic is dic2)
print("内置函数:")
li=list(range(10))
print(li)