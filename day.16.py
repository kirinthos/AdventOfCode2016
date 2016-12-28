#!/usr/bin/env python

value = "10001001100000001"
length = 35651584

def expand(a):
    borig = a[::-1]
    b = ''
    for c in borig:
        if c == '1':
            b = b + '0'
        else:
            b = b + '1'
    return a + '0' + b

def checksum(a):
    c = ''
    for i in range(0, len(a) - 1, 2):
        if a[i] == a[i+1]:
            c = c + '1'
        else:
            c = c + '0'
    return c

def expandToLength(a, l):
    c = a
    while len(c) < l:
        c = expand(c)
    c = c[:l]
    return c

expanded = expandToLength(value, length)
check = checksum(expanded)
while len(check) % 2 == 0:
    check = checksum(check)
print(check)
