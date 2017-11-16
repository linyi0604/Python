'''
python中内构函数非常多 
介绍常用的几个：

'''
'''
range(n)
'''
r = range( 11 )
print(r)
print(list(r))
for temp in r:
    print(temp,end=" ")
print()
'''
map(func,list)   对list的每一个元素按照func进行操作
'''
li = [ 1,2,3 ]
newL = map( lambda x:x*2  ,  li )
print( list(newL) )

#也可以传入两个列表  两个列表对应位置的元素分别进行操作
li2 = [4,5,6]
newL2 = map( lambda x,y:x+y , li , li2 )
print( list(newL2) )

'''
filter(func , list) 过滤器函数
            对list按照func进行过滤
'''
#过滤留下偶数
li3 = [1,2,3,4,5,6,7,8]
newL3 = filter( lambda x: not x%2 , li3 )
print(list( newL3 ) )

'''
reduce(func, list)  对list按照func进行累计操作 
        在python3中这个函数被迁移到了functools当中
'''
import functools
li4 = [1,2,3,4,5,6]
res = functools.reduce( lambda x,y:x+y , li4  )
print( res )