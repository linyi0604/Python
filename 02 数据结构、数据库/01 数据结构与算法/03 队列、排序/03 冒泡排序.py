#冒泡排序
# 9 6 7 5 8 4
def bubble_sort(li):
    n = len(li)
    for j in range(n-1):
        for i in range( n-1-j ):
            if li[i]>li[i+1]:
                li[i] , li[i+1] = li[i+1] , li[i]




if __name__ == '__main__':

    li = [ 9,6,7,5,8,4 ]

    bubble_sort(li)
    print(li)

    #最坏时间复杂度 O(n^2)
    #最优时间复杂度 O(n)
    #冒泡排序是稳定的