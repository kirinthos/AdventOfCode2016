#!/usr/bin/env python

screen = [ [ 0 for x in range(50) ] for y in range(6) ]

def rect(s, a, b):
    for row in range(b):
        for col in range(a):
            s[row][col] = 1


def rotateRow(s, row, moves):
    srow = s[row]
    l = len(srow)
    for i in range(moves):
        nextValue = srow[0]
        for j in range(l):
            jactual = (j + 1) % l
            tmp = srow[jactual]
            srow[jactual] = nextValue
            nextValue = tmp

def rotateColumn(s, col, moves):
    l = len(s)
    for i in range(moves):
        nextValue = s[0][col]
        for j in range(l):
            jactual = (j + 1) % l
            tmp = s[jactual][col]
            s[jactual][col] = nextValue
            nextValue = tmp

def printGrid(s):
    print('')
    for i in range(len(s)):
        tmp = ''
        for j in range(len(s[i])):
            if s[i][j] == 1:
                tmp = tmp + '#'
            else:
                tmp = tmp + '.'
        print(tmp)
    print('')

def countOnes(s):
    count = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 1:
                count = count + 1
    return count


with open('day.8.dat') as f:
    for line in f:
        components = line.replace('\n', '').split(' ')
        if components[0] == 'rect':
            pieces = components[1].split('x')
            x = int(pieces[0])
            y = int(pieces[1])
            rect(screen, x, y)
        else:
            x = int(components[2].split('=')[1])
            moves = int(components[4])
            if components[1] == 'row':
                rotateRow(screen, x, moves)
            else:
                rotateColumn(screen, x, moves)

printGrid(screen)
print(countOnes(screen))
