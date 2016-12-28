#!/usr/bin/env python

def printDiscs(discs):
    for d in discs:
        print(d)
    print('\n')

class Disc:
    def __init__(self, disc, nump, pos):
        self.discNumber = disc
        self.numPositions = nump
        self.startPosition = pos
        self.position = pos

    def advance(self):
        self.position = (self.position + 1) % self.numPositions

    def reset(self, base):
        self.position = (self.startPosition + base) % self.numPositions

    def __str__(self):
        return str(self.discNumber) + ": " + str(self.position)

discs = []
currentDisc = -1
with open('day.15.dat') as f:
    i = 1
    for line in f:
        splits = line.split(' ')
        numPositions = int(splits[3])
        position = int(splits[-1][:-2])
        discs.append(Disc(i, numPositions, position))
        i = i + 1

startTime = 0
while True:
    success = True
    for d in discs:
        d.reset(startTime)
    for steps in range(len(discs)):
        for d in discs:
            d.advance()
        if discs[steps].position != 0:
            success = False
            break
    if success:
        print('success')
        break
    startTime = startTime + 1
    currentDisc = -1

print(startTime)
