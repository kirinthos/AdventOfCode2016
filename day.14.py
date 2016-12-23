#!/usr/bin/env python

import hashlib

hashes = dict()
validKeys = []
puzzle = 'zpqevtbw'
index = 0

def containsTriplet(h):
    for i in range(len(h) - 2):
        if h[i] == h[i+1] and h[i] == h[i+2]:
            return h[i]
    return None

def containsQuintet(h, c):
    for i in range(len(h) - 4):
        if h[i] == h[i+1] and h[i] == h[i+2] and h[i] == h[i+3] and h[i] == h[i+4]:
            return h[i]
    return None

def genHash(salt, index):
    if index in hashes:
        h = hashes[index]
    else:
        test = puzzle + str(index)
        m = hashlib.md5()
        m.update(test)
        h = m.hexdigest()
        hashes[index] = h
    return h

while len(validKeys) < 64:
    h = genHash(puzzle, index)
    c = containsTriplet(h)
    if c != None:
        for i in range(1000):
            h2 = genHash(puzzle, index + i + 1)
            if containsQuintet(h2, c):
                validKeys.append(h)
                print(h, index)
                break

    index = index + 1
