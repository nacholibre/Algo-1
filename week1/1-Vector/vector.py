

class Vector(object):
    START_CAPACITY = 20

    def __init__(self):
        self.index = 0
        self.vc = [None] * self.START_CAPACITY
        self.vcSize = 0

    def insert(self, index, value):
        if index > self.index:
            raise Exception('You can\'t add element if index is > currentVectorIndex')

        self.vc = self.vc[:index] + [value] + self.vc[index:-1]

        self.vcSize += 1
        self.index += 1

    def add(self, value):
        currentVCLength = len(self.vc)

        if self.index + 1 > currentVCLength:
            newVC = [None, ] * currentVCLength
            self.vc = self.vc + newVC

        self.vc[self.index] = value

        self.vcSize += 1
        self.index += 1

    def get(self, index):
        return self.vc[index]

    def remove(self, index):
        self.vc = self.vc[:index] + self.vc[index+1:] + [None]

        self.vcSize = self.vcSize - 1

        self.index = self.index - 1

    def pop(self):
        currentVCLength = len(self.vc)

        popped = self.vc[self.index-1]

        self.vc = self.vc[:self.index-1]

        newVCLen = len(self.vc)
        self.vc = self.vc + [None] * (currentVCLength - newVCLen)

        self.index = self.index - 1

        self.vcSize = self.vcSize - 1

        return popped

    def size(self):
        return self.vcSize

    def capacity(self):
        return len(self.vc)

    def printVector(self):
        print 'Vector:', self.vc

    def getIndex(self):
        return self.index


if __name__ == '__main__':
    myVector = Vector()

    # for x in range(0, 25):
    #     myVector.add('numberOne')

    myVector.add('numberOne')
    myVector.add('numberTwo')
    myVector.add('numberThree')
    myVector.add('numberFour')
    print 'popped:', myVector.pop()
    # myVector.add('numberTwo')
    # myVector.add('numberThree')

    # myVector.remove(0)

    # myVector.add('numberFour')

    # myVector.insert(5, 'Hello')

    print 'Size: ', myVector.size()
    print 'Capacity: ', myVector.capacity()
    print 'Vector:', myVector.printVector()
    print 'Vector Index:', myVector.getIndex()
