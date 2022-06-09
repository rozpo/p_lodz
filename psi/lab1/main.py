import time
# user defined
dataSize = 10
startingCity = 0
# 0 - no debug
# 1 - debug: greedy, a*
# 2 - debug: all (huge output)
debug = 0

# util functions
def createAllPermutations(size):
    from itertools import permutations 
    result = list(permutations(range(0, size)))
    return result

def finalizePath(inputData, start):
    result = []
    for i in range(len(inputData)):
        if inputData[i][0] == start:
            inputData[i] = inputData[i] + (start,)
            result.append(inputData[i])
    return result

def genData(size):
    import random
    result = []
    for i in range(size):
        temp = []
        temp.append(i)
        temp.append(random.randint(1, 101))
        temp.append(random.randint(1, 101))
        result.append(temp)
    return result

def calcDist(obj1, obj2):
    import math
    return math.sqrt( (math.pow(obj2[1] - obj1[1], 2)) + (math.pow(obj2[2] - obj1[2], 2)) )

def printPossiblePaths():
    print "================="
    print "possible paths"
    finalPaths = finalizePath(createAllPermutations(dataSize), startingCity)
    for x in range(len(finalPaths)):
        print finalPaths[x]

# brute force
def bruteForce(inputData):
    start = time.time()
    paths = finalizePath(createAllPermutations(dataSize), startingCity)
    result = 0
    bestPath = 0
    print "================="
    print "bruteForce"
    for i in range(len(paths)):
        fullPathLen = 0
        for j in range(len(paths[0]) - 1):
            fullPathLen += calcDist(inputData[paths[i][j]], \
                inputData[paths[i][j+1]])
            if debug >= 2:
                print "[", inputData[paths[i][j]][0], ",", \
                    inputData[paths[i][j+1]][0], "]=", \
                    round(calcDist(inputData[paths[i][j]], \
                    inputData[paths[i][j+1]]), 2)
        if debug >= 2:
            print paths[i], " = ", round(fullPathLen, 2)
        if (result == 0) or (result > fullPathLen):
            result = round(fullPathLen, 2)
            bestPath = paths[i]
    print "answer:", bestPath, "=", result
    end = time.time()
    print "time:", round((end - start), 5), "s"

# greedy
def greedy(inputData):
    start = time.time()
    result = 0
    print "================="
    print "greedy"

    visited = []
    for i in range(len(inputData)):
        if len(visited) > 0:
            shortest = 0
            node = 0
            for j in range(len(inputData)):
                if j not in visited:
                    tempResult = calcDist(inputData[visited[-1]], inputData[j])
                    if debug >= 1:
                        print visited[-1], "->", j, "=", round(tempResult, 2)
                    if (shortest == 0) or (shortest > tempResult):
                        shortest = tempResult
                        node = j
            result += shortest
        else:
            node = i
        visited.append(node)
    # calc return path
    tempResult = calcDist(inputData[visited[-1]], inputData[visited[0]])
    result += tempResult
    if debug >= 1:
        print visited[-1], "->", visited[0], "=", round(tempResult, 2)
    visited.append(visited[0])
    print "answer:", visited, "=", round(result, 2)
    end = time.time()
    print "time:", round((end - start), 5), "s"

# a*
def aStar(inputData):
    start = time.time()
    result = 0
    print "================="
    print "aStar"

    visited = []
    for i in range(len(inputData)):
        if len(visited) > 0:
            shortest = 0
            node = 0
            for j in range(len(inputData)):
                if j not in visited:
                    path = calcDist(inputData[visited[-1]], inputData[j])
                    heu = calcDist(inputData[j], inputData[visited[0]])
                    tempResult = path + heu
                    if debug >= 1:
                        print visited[-1], "->", j, "=", round(path, 2), "+", round(heu, 2), "=", round(tempResult, 2)
                    if (shortest == 0) or (shortest > tempResult):
                        shortest = tempResult
                        finalPath = path
                        node = j
            result += finalPath
        else:
            node = i
        visited.append(node)
    # calc return path
    path = calcDist(inputData[visited[-1]], inputData[visited[0]])
    result += path
    if debug >= 1:
        print visited[-1], "->", visited[0], "=", round(path, 2)
    visited.append(visited[0])
    print "answer:", visited, "=", round(result, 2)
    end = time.time()
    print "time:", round((end - start), 5), "s"

# main
print "================="
print "num | posX | posY"
cities = genData(dataSize)
for x in range(len(cities)):
    print cities[x]

if debug >= 2:
    printPossiblePaths()
bruteForce(cities)
greedy(cities)
aStar(cities)