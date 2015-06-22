class HeapSort:

    # Sorts a sequence of integers.
    def sort(sequence):
        pass


def getParent(heap, i):
    return heap[i/2]


def swapPoVerigata():
    pass


if __name__ == '__main__':
    lst = [5, 3, 10, 15, 25, 2, 12]

    heap = [None] * 20

    heapIndex = 1

    for x in range(len(lst)):
        currentElement = lst[x]

        heapIndex = x + 1
        heap[heapIndex] = currentElement

        parentIndex = heapIndex/2
        childIndex = heapIndex

        child = heap[childIndex]
        parent = heap[parentIndex]

        swapPosition = heapIndex

        if parent and child > parent:
            # swap
            heap[childIndex] = parent
            heap[parentIndex] = child
            # nextParentIndex = heapIndex-1/2
            # nextParent = heap[nextParentIndex]

    print lst
    print heap

    #     pass

    # heap[1] = lst.pop()

    # i = 2
    # heap[i] = lst.pop()

    # parent = i/2

    # def getParent(myList, i):
    #     return myList[i/2]

    # print getParent(lst, 3)
