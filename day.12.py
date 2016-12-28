#!/usr/bin/env python

reg = dict()

code = []
with open('day.25.dat') as f:
    for line in f:
        code.append(line.replace('\n', '').split(' '))

for j in range(1, 1000):
    reg['a'] = reg['b'] = reg['c'] = reg['d'] = 0
    reg['a'] = j
    previous = 1
    i = 0
    while i < len(code):
        split = code[i]
        asm = split[0]
        if asm == 'cpy':
            src = split[1]
            if src in reg:
                reg[split[2]] = reg[src]
            else:
                reg[split[2]] = int(src)
        elif asm == 'inc':
            reg[split[1]] = reg[split[1]] + 1
        elif asm == 'dec':
            reg[split[1]] = reg[split[1]] - 1
        elif asm == 'jnz':
            src = split[1]
            if src in reg:
                if reg[src] != 0:
                    i = i + int(split[2])
                    continue
            elif int(src) != 0:
                i = i + int(split[2])
                continue
        elif asm == 'out':
            src = split[1]
            val = 0
            if src in reg:
                val = reg[src]
            else:
                val = int(src)
            if val == previous or (val != 0 and val != 1):
                print('failure a = ' + str(j) + '...val = ' + str(val))
                break
            else:
                previous = val
        i = i + 1
