class _Node:
    def __init__(self, prevNode, nextNode, element):
        '''constructs a node with an element, a next node and a previous node'''
        self.__prev = prevNode
        self.__next = nextNode
        self.__element = element

    def get(self):
        '''returns the element at the node'''
        return self.__element

    def next(self):
        '''returns the next node'''
        return self.__next

    def prev(self):
        '''returns the previous node'''
        return self.__prev
    
    def setNext(self, node):
        '''sets the NextNode'''
        self.__next = node

    def setPrev(self, node):
        '''sets the PreviousNode'''
        self.__prev = node

class _Sentinel(_Node):
    def __init__(self):
        super().__init__(None, None, None)  

class DoubleLinkedList:
    def __init__(self):
        self.__header = _Sentinel()
        self.__trailer = _Sentinel()
        self.__header.setNext(self.__trailer)
        self.__trailer.setPrev(self.__header)
    
    def isEmpty(self):
        return self.__header.next() == self.__trailer

    def addFront(self, element):
        node = _Node(self.__header, self.__header.next(), element)
        self.__header.next().setPrev(node)
        self.__header.setNext(node)
        return self
    
    def addBack(self, element):
        node = _Node(self.__trailer.prev(), self.__trailer, element)
        node.prev().setNext(node)
        node.next().setPrev(node)
        return self

    def front(self):
        return self.__header.next().get()

    def back(self):
        return self.__trailer.prev().get()

    def removeFront(self):
        node = self.__header.next()
        node.prev().setNext(node.next())
        node.next().setPrev(node.prev())
        return node.get()
    
    def removeBack(self):
        node = self.__trailer.prev()
        node.prev().setNext(node.next())
        node.next().setPrev(node.prev())
        return node.get()