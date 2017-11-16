#插入排序
#第一次拿第一个数形成新的数列
#第二次拿第二个数，跟第一个数形成有序队列
#第三次 拿第三个数跟前两个数形成有序队列
#第n次拿第n个数跟前面的队列 插入正确的位置


def insert_sort(li):

    n = len(li)
    for j in range(1,n):
        for i in range( j,0,-1 ):
            if li[i]< li[i-1]:
                li[i] , li[i-1] = li[i-1] ,li[i]
            else :
                break



if __name__ == '__main__':
    li = [9,8,7,8,4,3]
    insert_sort(li)
    print(li)
    # 插入排序最坏时间复杂度O(n^2)
    # 最优时间复杂度O(n)
    # 插入排序是稳定的排序