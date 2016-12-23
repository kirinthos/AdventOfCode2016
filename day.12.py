#!/usr/bin/env python

reg = dict()
reg['a'] = reg['b'] = reg['c'] = reg['d'] = 0
reg['c'] = 1

code = []
with open('day.12.dat') as f:
    for line in f:
        code.append(line.replace('\n', '').split(' '))

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
    i = i + 1

print(reg)
