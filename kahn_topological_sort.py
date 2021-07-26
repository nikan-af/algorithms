from collections import defaultdict


def orderDependencyList(dependencyList):
    numberOfVertices = len(dependencyList)
    finalDependencyOrder = list()
    numVerticesVisited = 0

    reversedDependencies = defaultdict(list)

    in_degrees = dict()
    for vertix, listOfDependencies in dependencyList.items():
        in_degrees[vertix] = len(listOfDependencies)
        for dependency in listOfDependencies:
            reversedDependencies[dependency].append(vertix)

    queue = list()

    for vertix, in_degree in in_degrees.items():
        if in_degree == 0:
            queue.append(vertix)

    while queue:
        poppedVertix = queue.pop(0)
        finalDependencyOrder.append(poppedVertix)

        for dependency in reversedDependencies[poppedVertix]:
            in_degrees[dependency] -= 1

            if in_degrees.get(dependency) == 0:
                queue.append(dependency)

        numVerticesVisited += 1

    if numVerticesVisited != numberOfVertices:
        print("There is a cycle!!")
    else:
        print(finalDependencyOrder)


orderDependencyList({
    'a': ['c'],
    'c': [],
    'e': ['a', 'b'],
    'b': ['c'],
    'd': ['e', 'b'],
})
