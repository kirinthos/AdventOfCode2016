#!/usr/bin/env python

triangles = []
matrix = []

with open('day.3.dat') as f:
    for line in f:
        sides = [int(x) for x in line.replace('\n', '').split(' ') if x != '']
        matrix.append(sides)
        if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]:
                triangles.append(sides)

columns = [ [ x[0] for x in matrix ], [ x[1] for x in matrix ], [ x[2] for x in matrix ] ]
triangles = []

for col in columns:
    for i in range(0, len(col) - 2, 3):
        if i + 2 > len(col) - 1:
            break
        if col[i] + col[i+1] > col[i+2] and col[i+1] + col[i+2] > col[i] and col[i] + col[i+2] > col[i+1]:
            triangles.append([col[i], col[i+1], col[i+2]])


print(triangles)
print(len(triangles))
