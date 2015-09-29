import fileinput

if __name__ == '__main__':
    packMatrix = {}

    for i, line in enumerate(fileinput.input()):
        if i == 0:
            items, backpackCapacity = line.split(' ')
            items = int(items)
            backpackCapacity = int(backpackCapacity)

            for x in range(0, items+1):
                mylist = []
                for x2 in range(0, items+1):
                    mylist.append(None)
                packMatrix[x] = mylist

    print packMatrix
