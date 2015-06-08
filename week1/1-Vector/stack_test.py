from stack import Stack


if __name__ == '__main__':
    myStack = Stack()
    myStack.push('one')
    assert myStack.size() == 1

    myStack = Stack()
    myStack.push('one')
    myStack.push('two')
    myStack.push('three')
    assert myStack.pop() == 'three'
    assert myStack.pop() == 'two'
    assert myStack.pop() == 'one'

    print 'All tests passed, YAY'
