
class HeapSort:

    def __init__(self):
        self.mylist = [None]
        self.current = None
        self.root = None
        self.nextIndex = 1

    # Sorts a sequence of integers.
    def sort(self, sequence):
        for number in sequence:
            self.insert(number)

        sortedList = []

        while True:
            popped = self.remove()
            if not popped:
                break
            sortedList.append(popped)

        return sortedList

    def _parent(self, index):
        return self.mylist[index/2]

    def _parentIndex(self, index):
        return index/2

    def _root(self):
        return self.mylist[1]

    def _swap(self, currentIndex, parentIndex):
        self.mylist[currentIndex], self.mylist[parentIndex] = \
            self.mylist[parentIndex], self.mylist[currentIndex]

    def insert(self, number):
        self.mylist.append(number)

        currentIndex = self.nextIndex

        while self.mylist[currentIndex] != self._root() and \
                self.mylist[currentIndex] > self._parent(currentIndex):
            self._swap(currentIndex, self._parentIndex(currentIndex))
            currentIndex = self._parentIndex(currentIndex)

        self.nextIndex += 1

    def _getLeftChildIndex(self, index):
        return index*2

    def _getRightChildIndex(self, index):
        return index*2 + 1

    def _getLeftChild(self, parentIndex):
        index = parentIndex*2

        try:
            return self.mylist[index]
        except IndexError:
            return None

    def _getRightChild(self, parentIndex):
        index = (parentIndex*2) + 1
        try:
            return self.mylist[index]
        except IndexError:
            return None

    def _largerChildIndex(self, parentIndex):
        leftChild = self._getLeftChild(parentIndex)
        rightChild = self._getRightChild(parentIndex)

        if leftChild > rightChild:
            return parentIndex*2
        else:
            return (parentIndex*2) + 1

    def remove(self):
        if self.mylist[self.nextIndex - 1] is None:
            return None

        lastElement = self.mylist.pop(self.nextIndex - 1)
        self.nextIndex -= 1

        if len(self.mylist) is 1:
            return lastElement

        root = self.mylist[1]

        try:
            self.mylist[1] = lastElement
        except IndexError:
            return None

        currentIndex = 1
        while (self._getLeftChild(currentIndex) and self.mylist[currentIndex] < self._getLeftChild(currentIndex)) or \
                (self._getRightChild(currentIndex) and self.mylist[currentIndex] < self._getRightChild(currentIndex)):
            largerChildIndex = self._largerChildIndex(currentIndex)
            self._swap(currentIndex, largerChildIndex)
            currentIndex = largerChildIndex

        return root


if __name__ == '__main__':
    lst = [5, 3, 10, 15, 25, 2, 12, 30, 40, 45, 150, 500]

    heapSort = HeapSort()

    print heapSort.sort(lst)

    # heapSort.insert(2)
    # heapSort.insert(12)
    # heapSort.insert(30)
    # print heapSort.mylist
    # print 'remove: ', heapSort.remove()
    # print heapSort.mylist
    # heapSort.insert(30)
    # print heapSort.mylist
