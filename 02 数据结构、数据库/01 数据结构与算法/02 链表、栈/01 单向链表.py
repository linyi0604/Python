# 单向链表

#节点类
class Node(object):
    '''单链表节点'''
    def __init__(self ,item ):
        self.item = item
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self):
        self.__head = None

    def is_empty(self):
        '''是否为空'''
        return self.__head is None
    def add(self,item):
        '''头部添加元素'''
        temp = Node(item)
        temp.next = self.__head
        self.__head = temp
    def append(self , item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.add(item)
        else :
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def length(self):
        '''链表长度'''
        current = self.__head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        '''遍历链表'''
        current = self.__head
        while current is not None :
            print(current.item, end= " ")
            current = current.next
        print()
    def insert(self, pos , item ):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            index = 0
            while index < pos - 1 :
                cur = cur.next
                index += 1
            node = Node(item)
            node.next = cur.next
            cur.next = node
    def remove(self,item):
        '''置顶位置删除元素'''
        cur = self.__head
        pre = None
        while cur is not None:
            #找到要删除的元素
            if cur.item == item :
                #如果cur是头节点 此时没有pre
                if pre is None:
                    head = cur.next
                else:
                    pre.next = cur.next
                break
            pre = cur
            cur = cur.next
    def search(self , item):
        '''查询元素是否存在'''
        cur = self.__head
        while cur is not None:
            if item == cur.item:
                return True
            cur = cur.next
        return False

if __name__ =="__main__":
    sll = SingleLinkList()
    print(sll.is_empty())
    sll.add(3)
    sll.add(4)
    sll.add(5)
    print(sll.is_empty())
    sll.travel()
    print(sll.length())
    sll.append(1 )
    sll.travel()
    sll.insert(100,10)
    sll.insert(-5 , 10)
    sll.insert(2,10)
    sll.travel()
    sll.remove(4)
    sll.travel()