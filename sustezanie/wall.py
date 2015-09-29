import math
import sys
import fileinput


if __name__ == '__main__':
    maxHeight = 1
    colSum = 0

    dunoMat = {}

    for i, line in enumerate(fileinput.input()):
        line = line.strip()
        if i == 0:
            size, cubicLitres = line.split(' ')
            size = int(size)
            cubicLitres = int(cubicLitres)
        else:
            dunoMat[i] = []
            cols = line.split(' ')
            for col in cols:
                col = int(col)
                dunoMat[i].append(col)

    for colNumber in dunoMat.iterkeys():
        for cell in dunoMat[colNumber]:
            if cell > maxHeight:
                maxHeight = cell

    totalAmountCanHandle = 0
    for colNumber in dunoMat.iterkeys():
        for cell in dunoMat[colNumber]:
            totalAmountCanHandle += (maxHeight - cell)

    atLeastPossibleHeight = maxHeight + 1

    # print maxHeight
    # print totalAmountCanHandle
    maxCapacity = totalAmountCanHandle
    # print dunoMat
    atLeastPossibleHeight = maxHeight + 1

    colSum = colSum * 1.0
    size = size * size * 1.0
    # print 'colSum', colSum
    # print 'pollsize', size

    # print size, cubicLitres
    # print 'maxHeight', maxHeight

    # maxCapacity = math.ceil(colSum/size) * size
    # print 'max capacity cubic litres', maxCapacity
    # print 'cubic litres to pour', cubicLitres

    # print cubicLitres - maxCapacity
    # print (cubicLitres - maxCapacity)/25

    neededCapacity = cubicLitres - maxCapacity
    # print 'needed', neededCapacity
    if neededCapacity < 0:
        print atLeastPossibleHeight
    else:
        needed = math.ceil(neededCapacity / size)
        print int(needed + atLeastPossibleHeight)

    sys.exit()

    # wallHeight = int(math.ceil(maxHeight + (cubicLitres - maxCapacity)/size))
    # if (wallHeight < atLeastPossibleHeight):
    #     print atLeastPossibleHeight
    # else:
    #     print wallHeight
