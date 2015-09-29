

# newDiscovered = set()
# newDiscoveredList = []
#
# def DFSRec(data, v):
#     newDiscovered.add(v)
#     newDiscoveredList.append(v)
#
#     for edge in data[v][1]:
#         if edge not in newDiscovered:
#             DFSRec(data, edge)

# def iterative_dfs(graph, start, path=[]):
#     '''iterative depth first search from start'''
#     q = [start]
#     while q:
#         v = q.pop(0)
#         if v not in path:
#             path= path + [v]
#             q=graph[v]+q
#     return path


visited = {}
visitedList = []

def DFSR(data, startFrom):
    visited[startFrom] = True

    for edge in data[startFrom][1]:
        if edge not in visited:
            DFSR(data, edge)

    visitedList.append(startFrom)

def DFS(data, startFrom):
    stack = []
    stack.append(startFrom)

    discoveredList = []
    visited = {}

    while len(stack):
        v = stack.pop(0)
        discoveredList.append(v)

        for edge in data[v][1]:
            if edge not in visited:
                stack.append(edge)
                visited[edge] = True

        # if v not in visited:
        #     discoveredList.append(v)
        #     visited[v] = True


    return discoveredList


def DFSWorking(data, startFrom):
    s = []
    s.append(startFrom)

    discovered = {}

    discoveredList = []

    while len(s):
        v = s.pop()

        if v not in discovered:
            discovered[v] = True
            discoveredList.append(v)

            for edge in data[v][1]:
                s.append(edge)

    return discoveredList


if __name__ == '__main__':
    projects = ['Extensions', 'Interface', 'Core', 'Common', 'Networking']
    project = 'Interface'

    dependencies = [
        ['Common', 'Core', 'Networking'],
        ['Core', 'Common', 'Extensions', 'Networking'],
        [],
        ['Core'],
        ['Core', 'Common'],
    ]

    data = []

    for n, prj in enumerate(projects):
        deps = dependencies[n]
        data.insert(n, [n, []])

        for dependency in deps:
            depIndex = projects.index(dependency)
            data[n][1].append(depIndex)

        # print deps
        # print n, project

    print data
    print '=' * 20
    DFSR(data, 1)

    # print project
    for i in visitedList:
        print projects[i]
    # print projects
    # print dependencies
