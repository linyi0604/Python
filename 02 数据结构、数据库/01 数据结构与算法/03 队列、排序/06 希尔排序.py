#希尔排序
# 按步长对插入排序进行了优化

#[ 9,8,7,8,4,3 ]

def shell_sort(li):
    n = len(li)
    gap = n//2
    while gap >= 1 :

        for j in range(gap,n):
            i = j
            while i-gap>=0 :
                if li[i] < li[i-gap] :
                    li[i],li[i-gap] = li[i-gap] , li[i]
                    i -= gap
                else :
                    break


        gap //= 2



if __name__ == '__main__':
    li = [6,4,3,9,1,7]
    shell_sort(li)
    print(li)
    #希尔排序  O(n)< x < O(n^2)
    #稳定性 不稳定










