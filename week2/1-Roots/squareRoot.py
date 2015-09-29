import random
import math
import roots


def linearSearch(wholeList, needle):
    found = False

    for elem in wholeList:
        if elem is needle:
            found = True
            break

    return found


def binarySearchNoRecursion(mylist, needle):
    left = 0
    right = len(mylist)
    found = False

    while left <= right and not found:
        middlePos = (right + left) / 2
        middleElement = mylist[middlePos]

        if middleElement == needle:
            found = True
        elif needle < middleElement:
            right = middlePos
        elif needle > middleElement:
            left = middlePos

    return found


def binarySearch(wholeList, needle, left=None, right=None, c=0):
    # if (c > 20):
    #     print '20 recursion'
    #     return

    if left is None and right is None:
        left = 0
        right = len(wholeList)

    middlePos = (right + left) / 2

    if left is right:
        return False

    middleElement = wholeList[middlePos]

    if middleElement == needle:
        return True
    elif needle < middleElement:
        right = middlePos
    elif needle > middleElement:
        left = middlePos
    else:
        raise Exception('this should not happen')

    c = c + 1
    return binarySearch(wholeList, needle, left, right, c)


def generateRandomSortedList():
    lst = []

    for x in range(0, random.randint(1, 6000)):
        lst.append(random.randint(0, 10000))

    return sorted(lst)


def testBinarySearchWithLinear():
    myLst = [1, 50, 150, 200, 202, 230, 250, 300]
    assert binarySearch(myLst, 1) is True
    assert binarySearch(myLst, 300) is True

    lst = generateRandomSortedList()

    for x in range(0, 100):
        randomElementFromList = random.choice(lst)
        assert linearSearch(lst, randomElementFromList) is binarySearchNoRecursion(lst, randomElementFromList)
        assert linearSearch(lst, randomElementFromList) is binarySearch(lst, randomElementFromList)

    lst = generateRandomSortedList()
    for needle in lst:
        assert linearSearch(lst, needle) is True
        assert binarySearchNoRecursion(lst, needle) is True
        assert binarySearch(lst, needle) is True


def testLinearSearch():
    mylst = [1, 7, 10, 25, 40, 89, 99, 150, 200, 270]

    assert linearSearch(mylst, 10) is True
    assert linearSearch(mylst, 270) is True
    assert linearSearch(mylst, 7) is True
    assert linearSearch(mylst, 1) is True
    assert linearSearch(mylst, 500) is False

    lst = generateRandomSortedList()

    for x in range(0, 100):
        randomElementFromList = random.choice(lst)
        assert linearSearch(lst, randomElementFromList) is True


def squareRootBinarySearch(number):
    left = 0
    right = number

    found = False

    c = 0

    closest = None

    while (right - left) >= 0.000001 and not found and c <= 100:
        c += 1
        middlePos = float(right + left) / 2
        middleElement = middlePos

        middleElementPow = math.pow(middleElement, 2)

        closest = middleElement

        if middleElementPow == number:
            found = middleElement
        if number < middleElementPow:
            right = middlePos
        elif number > middleElementPow:
            left = middlePos

    print 'total searches: %s' % c
    if found:
        return found
    else:
        return closest


if __name__ == '__main__':
    roots = roots.Roots()
    print roots.square_root(247359)
    # print squareRootBinarySearch(6000)

    # print 'tests passed yay!'
