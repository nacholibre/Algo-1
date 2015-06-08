from vector import Vector


if __name__ == '__main__':
    myVector = Vector()
    myVector.add('numberOne')
    assert myVector.size() == 1
    assert myVector.capacity() == 20

    myVector = Vector()
    myVector.add('numberOne')
    myVector.add('numberTwo')
    assert myVector.size() == 2
    assert myVector.capacity() == 20

    myVector = Vector()
    myVector.add('numberOne')
    assert myVector.pop() == 'numberOne'
    assert myVector.size() == 0
    assert myVector.capacity() == 20

    myVector = Vector()
    myVector.add('numberOne')
    myVector.add('numberTwo')
    assert myVector.pop() == 'numberTwo'
    assert myVector.pop() == 'numberOne'
    assert myVector.size() == 0
    assert myVector.capacity() == 20

    myVector = Vector()
    myVector.insert(0, 'Hello')
    assert myVector.size() == 1
    assert myVector.capacity() == 20
    assert myVector.pop() == 'Hello'
    assert myVector.get(0) is None
    assert myVector.size() == 0
    assert myVector.capacity() == 20

    myVector = Vector()
    myVector.add('Hello')
    myVector.add('Hello2')
    myVector.remove(0)
    assert myVector.get(0) == 'Hello2'
    assert myVector.size() == 1
    assert myVector.capacity() == 20

    myVector = Vector()
    myVector.add('Hello')
    myVector.add('Hello2')
    myVector.remove(1)
    assert myVector.get(0) == 'Hello'
    assert myVector.size() == 1
    assert myVector.capacity() == 20

    print 'All tests passed, YAY!'
