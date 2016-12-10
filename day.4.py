#!/usr/bin/env python

class Code:
    def __init__(self, line):
        self.map = dict()
        self.hashCode = line[line.find('[') + 1:len(line) - 2]
        
        

with open('day.4.dat') as f:
    for line in f:
        c = Code(line)
