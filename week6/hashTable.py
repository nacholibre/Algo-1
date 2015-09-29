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
