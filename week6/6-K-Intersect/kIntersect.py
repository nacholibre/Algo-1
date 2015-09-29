import sys


class HashTable():
    def __init__(self, maxMod):
        self.maxMod = maxMod
        self.hashSpace = [None] * self.maxMod

    def _hash(self, number):
        return number % self.maxMod

    def add(self, number):
        hashPos = self._hash(number)

        hashPositionVal = self.hashSpace[hashPos]

        if type(hashPositionVal) is int:
            self.hashSpace[hashPos] += 1
        elif hashPositionVal is None:
            self.hashSpace[hashPos] = 1

        return self.hashSpace[hashPos]

    def get(self, number):
        hashPos = self._hash(number)

        return self.hashSpace[hashPos]


if __name__ == '__main__':
    hashTable = HashTable(1000)

    numberOfLists = 0
    for i, line in enumerate(sys.stdin):
        if i is 0:
            numberOfLists = int(line)
            continue

        for num in line.split(' '):
            num = int(num)

            if hashTable.add(num) is numberOfLists:
                print num
