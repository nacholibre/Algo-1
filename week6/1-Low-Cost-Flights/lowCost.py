import fileinput
import copy


def readInput(myinput):
    edges = []

    queries = []

    airportsNumber = 0
    lineNumber = 0

    edgeWeights = {}

    for line in myinput:
        line = line.strip()

        if lineNumber == 0:
            airportsNumber = int(line)
            lineNumber += 1
            continue

        if lineNumber < (airportsNumber+1) and lineNumber != 0:
            vIndex = lineNumber-1
            edges.append([])

            for i, price in enumerate(line.split(' ')):
                price = int(price)
                if price == 0:
                    weight = float('+inf')
                else:
                    weight = price

                edges[vIndex].append(weight)
                edgeWeights[vIndex] = {i: weight}
        elif lineNumber == (airportsNumber + 1):
            pass
        else:
            split = line.split(' ')
            # print split
            queries.append((int(split[0]), int(split[1])))

        lineNumber += 1

    return (edges, queries, edgeWeights)


def shortestPath(edges, queries):
    newEdges = copy.copy(edges)

    for v, edge in enumerate(newEdges):
        newEdges[v][v] = 0

    for k, edge in enumerate(newEdges):
        for i, edge in enumerate(newEdges):
            for j, edge in enumerate(newEdges):
                if newEdges[i][j] > (newEdges[i][k] + newEdges[k][j]):
                    newEdges[i][j] = newEdges[i][k] + newEdges[k][j]

    # for v, u in enumerate(newEdges):
    #     for i, edge in enumerate(u):
    #         newEdges[i][
    #         print i
    #         print edge

    # for uIndex, edge in enumerate(newEdges):
    #     for u, weight in edge:
    #         print u, weight

    for myfrom, mytwo in queries:
        res = newEdges[myfrom][mytwo]
        if res == float('inf'):
            print 'NO WAY'
        else:
            print res


if __name__ == '__main__':
    edges, queries, weights = readInput(fileinput.input())

    shortestPath(edges, queries)

    # edges.append([])
    # edges[0].append((1, 9))
    # edges[0].append((3, 3))
    # edges[0].append((4, 2))

    # edges.append([])
    # edges[1].append(())

    # print edges
