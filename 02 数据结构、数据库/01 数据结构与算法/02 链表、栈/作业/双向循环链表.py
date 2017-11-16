#链表的节点
class Node(object):
    def __init__(self , item ):
        self.item = item    #节点数值
        self.prev = None    #用于指向前一个元素
        self.next = None    #用于指向后一个元素
#双向循环链表
class DoubleCircleLinkList(object):
    def __init__(self):
        self.__head = None  #初始化的时候头节点设为空、
    #判断链表是否为空，head为None 的话则链表是空的
    def is_empty(self):
        return self.__head is None
    #头部添加元素的方法
    def add(self,item):
        node = Node(item)   #新建一个节点node 里面的值是item
        # 如果链表是空的，则node的next和prev都指向自己(因为是双向循环)，head指向node
        if self.is_empty():
            self.__head = node
            node.next = node
            node.prev = node
        # 否则链表不空
        else:
            node.next = self.__head #node的next设为现在的head
            node.prev = self.__head.prev #node的prev 设为现在head的prev
            self.__head.prev.next = node  #现在head的前一个元素的next设为node
            self.__head.prev = node #现在head的前驱 改为node
            self.__head = node #更改头部指针
    #尾部添加元素方法
    def append(self , item):
        #如果当前链表是空的 那就调用头部插入方法
        if self.is_empty():
            self.add(item)
        #否则链表不为空
        else :
            node = Node(item)   #新建一个节点node
            #因为是双向循环链表，所以head的prev其实就是链表的尾部
            node.next = self.__head #node的下一个设为头
            node.prev = self.__head.prev    #node的前驱设为现在头部的前驱
            self.__head.prev.next = node    #头部前驱的后继设为node
            self.__head.prev = node #头部自己的前驱改为node
    #获得链表长度 节点个数
    def length(self):
        #如果链表是空的 就返回0
        if self.is_empty():
            return 0
        #如果不是空的
        else:
            cur = self.__head   #临时变量cur表示当前位置 初始化设为头head
            count = 1   #设一个计数器count，cur每指向一个节点，count就自增1  目前cur指向头，所以count初始化为1
            #如果cur.next不是head，说明cur目前不是最后一个元素，那么count就1，再让cur后移一位
            while cur.next is not self.__head:
                count += 1
                cur = cur.next
            #跳出循环说明所有元素都被累加了一次 返回count就是一共有多少个元素
            return count
    #遍历链表的功能
    def travel(self):
        #如果当前自己是空的，那就不遍历
        if self.is_empty():
            return
        #链表不空
        else :
            cur = self.__head   #临时变量cur表示当前位置，初始化为链表的头部
            #只要cur的后继不是头说明cur不是最后一个节点，我们就输出当前值，并让cur后移一个节点
            while cur.next is not self.__head:
                print( cur.item,end=" " )
                cur = cur.next
            #当cur的后继是head的时候跳出循环了，最后一个节点还没有打印值 在这里打印出来
            print( cur.item )

    #置顶位置插入节点
    def insert(self, pos , item ):
        #如果位置<=0 则调用头部插入方法
        if pos <= 0:
            self.add(item)
        #如果位置是最后一个或者更大 就调用尾部插入方法
        elif pos > self.length() - 1 :
            self.append(item)
        #否则插入位置就是链表中间
        else :
            index = 0   #设置计数器，用于标记我们后移了多少步
            cur = self.__head   #cur标记当前所在位置
            #让index每次自增1 ，cur后移，当index=pos-1的时候说明cur在要插入位置的前一个元素，这时候停下
            while index < pos - 1 :
                index += 1
                cur = cur.next
            #跳出循环，cur在要插入位置的前一个元素，将node插入到cur的后面
            node = Node(item) #新建一个节点
            node.next = cur.next    #node的后继设为cur的后继
            node.prev = cur #node的前驱设为cur
            cur.next.prev = node    #cur后继的前驱改为node
            cur.next = node #cur后继改为node
    #删除节点操作
    def remove(self,item):
        #如果链表为空 直接不操作
        if self.is_empty():
            return
        #链表不为空
        else:
            cur = self.__head   #临时变量标记位置，从头开始
            #如果头结点就是 要删除的元素
            if cur.item == item:
                #如果只有一个节点 链表就空了 head设为None
                if self.length() == 1:
                    self.__head = None
                #如果多个元素
                else:
                    self.__head = cur.next #头指针指向cur的下一个
                    cur.next.prev= cur.prev #cur后继的前驱改为cur的前驱
                    cur.prev.next = cur.next #cur前驱的后继改为cur的后继
            #否则 头节点不是要删除的节点 我们要向下遍历
            else:
                cur = cur.next  #把cur后移一个节点
                #循环让cur后移一直到链表尾元素位置，期间如果找得到就删除节点，找不到就跳出循环，
                while cur is not self.__head:
                    #找到了元素cur就是要删除的
                    if cur.item == item:
                        cur.prev.next = cur.next    #cur的前驱的后继改为cur的后继
                        cur.next.prev = cur.prev    #cur的后继的前驱改为cur的前驱
                    cur = cur.next
    #搜索节点是否存在
    def search(self , item):
        #如果链表是空的一定不存在
        if self.is_empty():
            return False
        #否则链表不空
        else:
            cur = self.__head   #设置临时cur从头开始
            # cur不断后移，一直到尾节点为止
            while cur.next is not self.__head:
                #如果期间找到了就返回一个True 结束运行
                if cur.item == item:
                    return True
                cur = cur.next
            # 从循环跳出来cur就指向了尾元素 看一下为元素是不是要找的 是就返回True
            if cur.item ==item:
                return True
            #所有元素都不是 就返回False 没找到
            return False


if __name__ == "__main__":
    dlcl = DoubleCircleLinkList()
    print(dlcl.search(7))
    dlcl.travel()
    dlcl.remove(1)
    print(dlcl.length())
    print(dlcl.is_empty())
    dlcl.append(55)
    print(dlcl.search(55))
    dlcl.travel()
    dlcl.remove(55)
    dlcl.travel()
    print(dlcl.length())
    dlcl.add(3)
    print(dlcl.is_empty())
    dlcl.travel()
    dlcl.add(4)
    dlcl.add(5)
    dlcl.append(6)
    dlcl.insert(-10,1)
    dlcl.travel()
    print(dlcl.length())
    dlcl.remove(6)
    dlcl.travel()

    print(dlcl.search(7) )
    dlcl.append(55)
    dlcl.travel()

