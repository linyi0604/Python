'''
之前分析了好多排序算法，可难理解了呢！！（泣不成声）
这次我要把二分查找总结一下，这个算法不算难度特别大，欢迎大家参考借鉴

我不喜欢太官方的定义，太晦涩的语言，让人看了就头晕。我希望加入我自己的理解，能帮助大家更好的理解算法的原理
同时也欢迎大家批评指正

二分查找:
    我们手里有一个长度为n的正序数列，当我们想查找一个数 x是否在这个数列当中的时候
    1 取数列正中间的数mid，
        如果mid和x相等，则找到结果，查找成功 返回True
        如果mid比x大，则x应该在mid的左侧，我们把mid左侧当作一个新的数列li
        如果mid比x小，则x应该在mid的右侧，我们把mid右侧当作一个新的数列li
    2 对于新的数列li 进行1的查找工作
    
    3 一直重复上面查找，生成新的数列li为空的时候则 数列当中没有数x 返回False

时间复杂度：最优O(1)   我们取第一次中间数mid 找到了 这种概率很低
        最坏O(log n)  假设n个数的数列，每次把数列分成两半，n除以多少次2 等于1 呢？  log n次

'''


#递归实现二分查找 li是列表   item是要查找的元素
# def merge_search( li ,item ):
#     #传来的列表每次都是新生成的，如果发现里面没有元素，则是查找到尽头都没找到
#     if not li :
#         return False
#
#     mid = len(li)//2   #mid记录li的中间位置
#     #检查一下 如果中间这个数就是要找的元素 返回真
#     if li[mid] == item :
#         return True
#     # 如果mid比item大，说明item可能会出现在mid左边，对左边再查找
#     elif li[mid]> item :
#         return merge_search( li[:mid] ,item )
#     # mid 比item小，说明item有可能在mid右边，对右边再查找
#     else :
#         return merge_search( li[mid+1:] , item )

# if __name__ == '__main__':
#     li = [1,2,3,4,5,6,7]
#     print( merge_search(li , 0) )   #False
#     print( merge_search(li , 1) )   #True


def merge_search( li , item ):
    #获取li的开始 结束
    start = 0
    end = len(li)-1

    #只要start和end 还没错开 就一直找
    while start <= end :
        #通过计算获取当前查找范围的中间位置
        mid = (start + end)//2
        #如果中间数就是item则返回True
        if li[mid] == item :
            return True
        #如果mid比item大，说明item可能会出现在mid左边，对左边再查找
        elif li[mid]> item :
            end = mid - 1
        # mid 比item小，说明item有可能在mid右边，对右边再查找
        else :
            start = mid + 1
    #跳出循环说明没找到 返回错误
    return False

if __name__ == '__main__':
    li = [1,2,3,4,5,6,7,8]
    print( merge_search(li , 8) ) #True
    print( merge_search(li , 0) ) #False