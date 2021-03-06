'''

快速排序是当下面试最容易考的题之一。初学算法基础的伙伴一定饱受它的折磨，因为快速排序的思想让初学者有一些发懵。
我写下这篇文章谈一谈自己对快速排序的理解，希望能够帮助初学者理解一下快速排序算法的流程。

快速排序的思想:
    我要探讨的思想呢，不是教科书上的，而是我自己按容易理解的方法进行了改编。
    请大家跟着我的思路：

宏观的来看：
        1 我们拿出第一个数当作基准数，把所有比他小的数放在他左边，所有比他大的数放在右边
        2 对mid左侧所有的数当成一个新的数列 进行上述排序
        3 对mid右侧所有的数当成一个新的数列 进行上述排序

        一个大数列，一点一点被我们分的越来越小，最后找到一个数做mid排完之后，左侧就剩下一个数，右侧就剩下一个数，就排完了

具体怎么实现找到基准数位置的呢？？
    我们拿到一个数列有n个数， 我们假设面前摆了n个水桶，每个水桶里面有一个数，现在数是乱序的，我们要不移动水桶，而把数取出来排序。
    我们把n个水桶从左到右编号分别为0到n-1
    ok！！！请大家跟着我的步骤哦~不要掉队！！
    1 把0号水桶的数拿在手里， 这个数，我们把它当作基准数mid
    2 拿一个名字叫做high的水瓶子当作标记，从最右侧n-1号桶开始往左找，找到第一个比基准数mid小的数的时候，我们把这个数取出来，放在0号位置，把high放进这个水桶里，标记一下现在这个水桶空了。
    3 拿另一个名字为low的水瓶子当作标记，从刚才把high所在桶取出的数扔进的那个桶开始向右找，找到第一个比mid大的数，我们把low水瓶扔进去把数取出来，把这个数扔进high水瓶所在的桶里。
    4 从刚刚取出high的水桶开始向左找，找到第一个比基准数mid小的数，把high瓶子扔进去把数取出来，然后把数扔进low瓶子所在的桶里，把low瓶子取出来
    5 从刚取出low的桶开始向右找，找到第一个比基准数mid小的数，把low扔进桶，把数取出来放进high瓶子所在桶里，把high瓶子取出来
    6 从刚取出high的桶向左找，找到第一个比基准数mid大的数，把high扔进去，把数取出来放到low所在的桶里，把low拿出来
    7 从刚取出low的桶向右找，找到第一个比基准数mid小的数，把low扔进去，把数取出来放进high瓶子所在桶里，把high取出来
    .......
    我们发现从2到7 一直在做相同的工作，右侧的high水瓶子在一点一点向左推进，左侧的low水瓶子在不断向右推进
    最后 low和high两个水平碰面了，我们把mid基准数放到这个碰面的水桶里
    此时，mid左侧的数全都比mid小
        mid右侧的数全都比mid大

    然后，对mid 左侧所有的数当作一个新的数列，进行刚刚的排序
        再对mid右侧所有的数当作一个新的数列，进行刚刚的操作

    这样一直重复下去，数列就被排好了。

    我们简化一下刚刚的步骤：
        1 把第一个数当作基准数mid拿出来，0号位置空了
        2 从右侧向左找第一个比基准数小的数记录位置high，把数拿出来放到mid所在位置上，high位置空了
        3 mid右侧第一个向右找第一个比基准数大的数记录位置low，把数拿出来放到high空位上， 这时候左边low位置空了
        4 从high开始向左找，找到第一个比mid小的数high重新记录位置，把数取出来放到low位置上，high位置空了
        5 从low开始向右找，找到第一个比mid大的数low重新记录位置，把数取出来放到high位置上，low位置空了
        ....之后我们一直重复
        low一点点向右，high一点点向左
        当low和high碰头的时候，我们把mid放在碰头位置上
        这时候形成的局面就是，mid左侧的数全都比mid小，mid右侧的数全都比mid大
        然后我们把mid左侧所有数当成新的数列进行上述排序
        把mid右侧所有数当成新的数列进行上述排序

        这样一直重复下去，每次数列都被裁剪成更小的数列，一直到我们拿出第一个数做基准数，我发现右侧没有数左侧也没有数，这个数列排序结束了


    但是我们刚刚忽略了一个严重的问题！！！！我们把比mid小的数放在左侧，把比mid大的数放在右侧了！那和mid相等的呢？？？？
            如果我们在两侧遇到mid相等的数，都移动到另一侧，实际上在程序中会陷入死循环，
                每次都拿出数放入对面的空位，对面从空位开始比较又扔了回来
        所以怎么办！！？？
        其实，当两边碰到相等都不管，或者只有一侧进行移动到另一侧，另一侧不管，这样最终排序就能正确。
            如果我们都不管相等的数，再排子数列的时候，会判断出他是最大或者最小，再被移动到相应位置。

时间复杂度：
    最坏时间复杂度： O(n^2) 我们假设拿到一个正序，每次拿到的基准数比较之后都没移动，所有的数都参与了比较，那就相当于每个数都跟其他所有数比了一次
    最优时间复杂度： O(n log n) 
        我们粗略理解成每次把数列分成两半的话，一共会分多少次呢？就看长度n除以2 要除x次后n为1，x=log n
        每次分开的数列n个数每个都跟基准数比了一次 所以粗略看成 是 n log n
稳定性： 不稳定
    从我们刚才探讨的，碰到和基准数相等的问题上就能看出快速排序不稳定



我们上代码！！！    
在python中这样实现
'''


# 快速排序 传入列表、开始位置和结束位置
def quick_sort(li, start, end):
    # 如果start和end碰头了，说明要我排的这个子数列就剩下一个数了，就不用排序了
    if not start < end:
        return

    mid = li[start]  # 拿出第一个数当作基准数mid
    low = start  # low来标记左侧从基准数始找比mid大的数的位置
    high = end  # high来标记右侧end向左找比mid小的数的位置

    # 我们要进行循环，只要low和high没有碰头就一直进行,当low和high相等说明碰头了
    while low < high:
        # 从high开始向左，找到第一个比mid的数，标记位置,（如果high的数大于等于mid，我们就左移high）
        # 并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low < high and li[high] >= mid:
            high -= 1
        # 跳出while后，high所在的下标就是找到的右侧比mid小的数
        # 把找到的数放到左侧的空位 low 标记了这个空位
        li[low] = li[high]
        # 从low开始向右，找到第一个比mid大的数，标记位置,（如果low的数小于等于mid，我们就右移low）
        # 并且我们要确定找到之前，如果low和high碰头了，也不找了
        while low < high and li[low] <= mid:
            low += 1
        # 跳出while循环后low所在的下标就是左侧比mid大的数所在位置
        # 我们把找到的数放在右侧空位上，high标记了这个空位
        li[high] = li[low]
        # 以上我们完成了一次 从右侧找到一个小数移到左侧，从左侧找到一个大数移动到右侧
    # 当这个while跳出来之后相当于low和high碰头了，我们把mid所在位置放在这个空位
    li[low] = mid
    # 这个时候mid左侧看的数都比mid小，mid右侧的数都比mid大

    # 然后我们对mid左侧所有数进行上述的排序
    quick_sort(li, start, low - 1)
    # 我们mid右侧所有数进行上述排序
    quick_sort(li, low + 1, end)


# ok我们实践一下
if __name__ == '__main__':
    li = [5, 4,1, 3, 5 ,4, 2, 1, 3 ,5]
    quick_sort(li, 0, len(li) - 1)
    print(li)