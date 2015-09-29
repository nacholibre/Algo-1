import fileinput

if __name__ == '__main__':
    matrixPath = {}

    filledMatrix = {}

    rows = 0

    row = 0
    for i, line in enumerate(fileinput.input()):
        line = line.strip()
        if i == 0:
            rows = int(line) - 1
            continue

        matrixPath[row] = [int(x) for x in line.split(' ')]
        filledMatrix[row] = [None for x in line.split(' ')]
        row += 1

    startRow = rows
    startCol = 0

    for col, bananas in enumerate(matrixPath[startRow]):
        if col == 0:
            filledMatrix[startRow][col] = bananas
        else:
            filledMatrix[startRow][col] = bananas + filledMatrix[startRow][col-1]

    for row in range(startRow, -1, -1):
        if row == rows:
            continue

        bananas = matrixPath[row][0]
        filledMatrix[row][0] = bananas + filledMatrix[row+1][0]

    for row in range(startRow-1, -1, -1):
        for colIndex, column in enumerate(filledMatrix[row]):
            if colIndex == 0:
                continue
            cellBananas = matrixPath[row][colIndex]
            leftBananas = filledMatrix[row][colIndex-1]
            bottomBananas = filledMatrix[row+1][colIndex]

            maxBanana = max(leftBananas, bottomBananas)
            filledMatrix[row][colIndex] = cellBananas + maxBanana

    print filledMatrix[0][rows]
