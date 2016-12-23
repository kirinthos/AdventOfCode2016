#!/usr/bin/env python

import math
from pprint import pprint

def convertBin(num):
    n = num
    t = int(math.ceil(math.log(num, 2))) + 1
    r = range(t)
    r.reverse()
    s = ''
    for i in r:
        val = math.pow(2, i)
        if n >= val:
            n = n - val
            s = s + '1'
        else:
            s = s + '0'
    return s


def checkSpace(x, y, num):
    val = x * x + 3 * x + 2 * x * y + y + y * y + num
    b = convertBin(val)
    count = 0
    for c in b:
        if c == '1':
            count = count + 1
    return (count % 2) == 0

def generateMaze(w, h, num):
    m = []
    for y in range(h):
        m.append([])
        for x in range(w):
            m[y].append(checkSpace(x, y, num))
    return m

def printMaze(m):
    for y in range(len(m)):
        s = ''
        for x in range(len(m[y])):
            if m[y][x]:
                s = s + '.'
            else:
                s = s + '#'
        print(s)
    print('\n')

def findNeighbors(distanceMap, loc, num):
    neighbors = []
    d = distanceMap[loc[1]][loc[0]]
    if checkSpace(loc[0] - 1, loc[1], num) and distanceMap[loc[1]][loc[0] - 1] > d + 1:
        neighbors.append([ loc[0] - 1, loc[1] ])
        distanceMap[loc[1]][loc[0] - 1] = d + 1
    if checkSpace(loc[0] + 1, loc[1], num) and distanceMap[loc[1]][loc[0] + 1] > d + 1:
        neighbors.append([ loc[0] + 1, loc[1] ])
        distanceMap[loc[1]][loc[0] + 1] = d + 1
    if checkSpace(loc[0], loc[1] - 1, num) and distanceMap[loc[1] - 1][loc[0]] > d + 1:
        neighbors.append([ loc[0], loc[1] + 1 ])
        distanceMap[loc[1] - 1][loc[0]] = d + 1
    if checkSpace(loc[0], loc[1] + 1, num) and distanceMap[loc[1] + 1][loc[0]] > d + 1:
        neighbors.append([ loc[0], loc[1] + 1 ])
        distanceMap[loc[1] + 1][loc[0]] = d + 1
    return neighbors

def bfs(m, loc, finish, num):
    # examine node, are we at end?
    # if not enqueue all neighbors
    #    adding the distance + 1 to the distance map
    distanceMap = [ [ 9999 for x in range(len(m[y])) ] for y in range(len(m)) ]
    toExamine = [ [ loc[0], loc[1] ] ]
    distanceMap[loc[1]][loc[0]] = 0
    while len(toExamine) > 0:
        pt = toExamine.pop(0)
        for n in findNeighbors(distanceMap, pt, num):
            toExamine.append(n)
        pprint(distanceMap)

    return distanceMap[finish[1]][finish[0]]

num = 1362
loc = [1, 1]
finish = [31, 39]
maze = generateMaze(50, 50, num)
printMaze(maze)
print(bfs(maze, loc, finish, num))
