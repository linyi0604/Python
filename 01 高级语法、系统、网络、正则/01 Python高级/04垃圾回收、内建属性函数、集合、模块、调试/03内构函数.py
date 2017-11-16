'''
python中常用的三个内构函数
'''
'''
range（）
'''
li = range(11)  #生成迭代器类型变量
print(li)
list = list(li) #生成列表
print(list)


'''
map(fun,list)   功能是对 传入的列表每一个元素进行相关操作
'''
#对每一个元元素*2
list = [1,2,3]
list2 = map( lambda x:x*2 , list)
for temp in list2:
    print(temp,end=" ")
print()
#两个列表元素相加
list=[1,2,3,4]
list2=[5,6,7,8]
list3 = map(lambda x,y:x+y,list ,list2 )
for temp in list3:
    print(temp,end=" ")
print()

'''
filter() 过滤器
'''
list = [1,2,3,4,5,6,7,8]
#过滤偶数 留下奇数
list1 = filter(lambda x:x%2 , list)
for temp in list1:
    print(temp,end=" ")
print()

'''
reduce() 函数  做累加操作
'''
import functools
#reduce 在python3被加入到functools 当中了
#做累加操作返回和
list = [1,2,3]
h =  functools.reduce( lambda x,y:x+y , list )
print(h)
#相当于在列表的第一项之前加上5
h =  functools.reduce( lambda x,y:x+y , list,5 )
print(h)