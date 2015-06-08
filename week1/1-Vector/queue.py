
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Queue(object):
    def __init__(self):
        self.qSize = 0
        self.lastElem = 0
        self.linkedList = None

    def push(self, element):
        myNode = Node(element)

        if self.qSize == 0:
            self.linkedList = myNode
        else:
            self.lastElem.setNext(myNode)

        self.qSize += 1

        self.lastElem = myNode

    def size(self):
        return self.qSize

    def peek(self):
        if self.qSize == 0:
            return None
        return self.linkedList.getData()

    def pop(self):
        if self.qSize == 0:
            return None
        self.qSize = self.qSize - 1

        currentData = self.linkedList.getData()

        if self.linkedList.getNext():
            self.linkedList = self.linkedList.getNext()

        return currentData
