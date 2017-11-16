# 单向链表

#节点类
class Node(object):
    '''单链表节点'''
    def __init__(self ,item ):
        self.item = item
        self.next = None

class SingleCircleLinkList(object):
    '''单链表'''
    def __init__(self):
        self.__head = None

    def is_empty(self):
        '''是否为空'''
        return self.__head is None

    def add(self,item):
        '''头部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node


    def append(self , item):
        '''尾部添加元素'''
        if self.is_empty():
            self.add(item)
        else :
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node = Node(item)
            node.next = self.__head
            cur.next = node

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next is not self.__head:
            count +=1
            cur = cur.next
        return count
    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return
        cur = self.__head
        print(cur.item,end=" ")
        while cur.next is not self.__head:
            cur = cur.next
            print(cur.item,end=" ")
        print()

    def insert(self, pos , item ):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            index = 0
            cur = self.__head
            while index < pos- 1:
                index += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node
    def remove(self,item):
        '''置顶位置删除元素'''
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head :
            if cur.item == item :
                if pre is None:
                    #删除头结点 需要把为节点指向新的头结点
                    tail = self.__head
                    while tail.next is not self.__head:
                        tail = tail.next
                    self.__head = cur.next
                    tail.next = self.__head
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next
        #处理尾节点
        if cur.item == item :
            if cur is self.__head:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self , item):
        '''查询元素是否存在'''
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item :
            return True
        while cur.next is not self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

if __name__ =="__main__":
    scsl = SingleCircleLinkList()
    print(scsl.length())
    scsl.append(50)
    scsl.add(1)
    scsl.add(2)
    scsl.add(3)
    print( scsl.is_empty() )
    scsl.travel()
    print(scsl.length())
    scsl.append(10)
    scsl.travel()
    scsl.insert(2,99)
    scsl.travel()
    print(scsl.search(3) )
    scsl.remove(99)
    scsl.travel()
