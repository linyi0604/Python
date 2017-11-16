class Node(object):
    '''双向链表节点'''
    def __init__(self ,item ):
        self.item = item
        self.prev = None
        self.next = None

class DoubleLinkList(object):
    '''双向链表'''
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
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self , item):
        '''尾部添加元素'''
        if self.is_empty():
            self.add(item)
        else :
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next=Node(item)
    def length(self):
        '''链表长度'''
        cur = self.__head
        count = 0
        while cur is not None:
            count +=1
            cur = cur.next
        return count
    def travel(self):
        '''遍历链表'''
        cur = self.__head
        while cur is not None:
            print(cur.item,end=" ")
            cur = cur.next
        print()
    def insert(self, pos , item ):
        '''指定位置添加元素'''
        if pos <= 0 :
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            cur = self.__head
            index = 0
            while index < pos -1:
                index += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next.prev = node
            cur.next=node
            node.prev = cur

    def remove(self,item):
        '''置顶位置删除元素'''
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                if cur is self.__head:
                    self.__head = cur.next
                else :
                    if cur.next is None:
                        cur.prev.next = None
                    else:
                        cur.next.prev = cur.prev
                        cur.prev.next = cur.next
                break
            cur = cur.next


    def search(self , item):
        '''查询元素是否存在'''
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    dll.add(3)
    dll.add(2)
    print(dll.is_empty())
    dll.travel()
    dll.append(5)
    dll.travel()
    print(dll.length())
    dll.insert(2,10)
    dll.travel()
    dll.remove(5)
    dll.travel()
    print(dll.search(1))