from queue import Queue


class Stack(object):
    def __init__(self):
        self.myQueue = Queue()
        self.mySize = 0

    def push(self, value):
        self.myQueue.push(value)
        self.mySize = self.mySize + 1

    def size(self):
        return self.mySize

    def peek(self):
        last = None

        while True:
            popped = self.myQueue.peek()

            if not popped:
                break

            last = popped

        return last

    def pop(self):
        last = None

        newQueue = Queue()

        poppedFromQueue = 0
        queueSize = self.myQueue.size()

        while True:
            popped = self.myQueue.pop()

            if poppedFromQueue != queueSize:
                newQueue.push(popped)

            poppedFromQueue += 1

            if not popped:
                break

            last = popped

        self.mySize = self.mySize - 1
        self.myQueue = newQueue
        return last
