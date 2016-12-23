#!/usr/bin/env python

def sortFunc(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return 0

data = None
with open('day.6.dat') as f:
    data = [x.replace('\n', '') for x in f.readlines()]

columnCount = len(data[0])
columns = [ [] for x in range(columnCount) ]

for line in data:
    for i in range(len(line)):
        columns[i].append(line[i])

for col in columns:
    chars = dict()
    for c in col:
        if c in chars:
            chars[c] = chars[c] + 1
        else:
            chars[c] = 1

    repeats = [ (k, v) for k, v in chars.items() ]
    repeats.sort(sortFunc)
    print(repeats[0][0])
