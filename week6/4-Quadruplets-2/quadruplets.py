import sys


class HashTable():
    def __init__(self):
        self.maxMod = 700
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

    def get(self, number):
        hashPos = self._hash(number)

        return self.hashSpace[hashPos]


def simpleHash(number, mod):
    return number % mod

if __name__ == '__main__':
    numbersList = []

    for i, line in enumerate(sys.stdin):
        if i is 0:
            continue
        line = line.strip()

        mylist = []

        for number in line.split(' '):
            mylist.append(int(number))

        numbersList.append(mylist)

    hashTable = HashTable()

    mylist1 = []
    for num in numbersList[0]:
        for num2 in numbersList[1]:
            mylist1.append(num + num2)
            hashTable.add(num + num2)

    found = 0
    mylist2 = []
    for num in numbersList[2]:
        for num2 in numbersList[3]:
            mylist2.append(num + num2)

            searchFor = (num + num2) * -1
            numFound = hashTable.get(searchFor)
            if numFound:
                found += numFound

    print found
