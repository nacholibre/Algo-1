from queue import Queue

if __name__ == '__main__':
    myQueue = Queue()
    myQueue.push('one')
    myQueue.push('two')
    assert myQueue.pop() == 'one'

    myQueue = Queue()
    myQueue.push('one')
    myQueue.push('two')
    assert myQueue.size() == 2
    assert myQueue.pop() == 'one'
    assert myQueue.pop() == 'two'
    assert myQueue.size() == 0

    myQueue = Queue()
    myQueue.push('one')
    myQueue.push('two')
    myQueue.push('three')
    assert myQueue.size() == 3
    assert myQueue.pop() == 'one'
    assert myQueue.peek() == 'two'
    assert myQueue.pop() == 'two'
    assert myQueue.pop() == 'three'

    myQueue = Queue()
    myQueue.push('one')
    assert myQueue.pop() == 'one'
    assert myQueue.pop() is None

    print 'All tests passed YAY!'
