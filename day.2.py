#!/usr/bin/env python

point = [-2, 0]
keys = []

with open('day.2.dat', 'r') as f:
    for line in f:
        for c in line:
            print(c)
            if c == 'U':
                point[1] = max(point[1] - 1, abs(point[0]) - 2)
                print(point, abs(point[0]) - 2)
            elif c == 'R':
                point[0] = min(point[0] + 1, 2 - abs(point[1]))
                print(point, 2 - abs(point[1]))
            elif c == 'D':
                point[1] = min(point[1] + 1, 2 - abs(point[0]))
                print(point, 2 - abs(point[0]))
            elif c == 'L':
                point[0] = max(point[0] - 1, abs(point[1]) - 2)
                print(point, abs(point[1]) - 2)

        keys.append((point[0], point[1]))


print(keys)
