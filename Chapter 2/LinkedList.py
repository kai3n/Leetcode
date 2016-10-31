
class LinkedList:

    class _Node:

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):

        if self._size == 0:
            return True
        else:
            return False

    def frontAdd(self,e):

        if self._size == 0:
            self._head = self._Node(e, None)
            self._size += 1
        else:
            a = self._Node(e, None)
            a._next = self._head
            self._head = a
            self._size += 1


    def backAdd(self,e):

        if self._size == 0:
            self._head = self._Node(e, None)

            self._size += 1
        else:
            tmp = self._head
            while tmp._next != None:
                tmp = tmp._next
            tmp._next = self._Node(e, None)
            self._size += 1

    def frontDel(self):
        self._head = self._head._next

    def get(self):
        tmp = self._head

    def get(self):
        tmp = self._head
        while tmp != None:
            print(tmp._element)
            tmp = tmp._next


a = LinkedList()
a.frontAdd(1)
a.frontAdd(3)
a.frontAdd(2)
a.frontAdd(6)
a.frontAdd(9)
a.backAdd(8)
a.frontDel()
a.backAdd(7)
a.get()
