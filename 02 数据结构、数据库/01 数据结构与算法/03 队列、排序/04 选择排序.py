#选择排序
# 9 7 8 6 3

def select_sort(li):
    n = len(li)
    #用j记录下表，从0开始 到最倒数第二个数为止
    for j in range( n-1 ):
        temp = j
        # temp记录j的位置，
        #i从当前j后面第一个数到最后，如果i记录的数小 temp指向i的位置
        for i in range(j+1, n ):
            if li[i] < li[temp]:
                temp = i
        #循环结束之后temp指向了j之后所有数中最小的 把最小的和j的位置换一下
        li[j],li[temp] = li[temp] , li[j]
    # 第一次排序保证了最小的数放在了0号位置
    # 第二次排序保证了第二小的数放在了1号位置
    # 第n次排序保证了 前n个数顺序是正确逇

if __name__ == '__main__':
    li = [9,7,8,6,3]
    select_sort(li)
    print(li)
    #最坏时间复杂度 O(n^2)
    #最优时间复杂度O(n^2)
    # 选择排序是不稳定的排序