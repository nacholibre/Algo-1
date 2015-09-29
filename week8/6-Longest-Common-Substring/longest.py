import fileinput

if __name__ == '__main__':
    matrixPath = {}

    buildedMatrix = {}

    lines = []

    maxLineWords = 0
    for line in fileinput.input():
        lines.append('0' + line.strip())

    for colIndex in range(0, len(lines[0])+1):
        matrixPath[colIndex] = []

        for rowIndex in range(0, len(lines[1])+1):
            matrixPath[colIndex].append(0)

    # print matrixPath
    for rowIndex in matrixPath.iterkeys():
        for colIndex, colData in enumerate(matrixPath[rowIndex]):
            if rowIndex == 0 or colIndex == 0:
                continue

            try:
                if lines[1][rowIndex] == lines[0][colIndex]:
                    # matrixPath[colIndex][rowIndex] = matrixPath[colIndex-1][rowIndex-1] + 1
                    matrixPath[colIndex][rowIndex] = matrixPath[colIndex-1][rowIndex-1] + 1
            except:
                continue

    for i, k in enumerate(matrixPath.iterkeys()):
        print i, matrixPath[k]
