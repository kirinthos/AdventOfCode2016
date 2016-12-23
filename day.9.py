#!/usr/bin/env python

line = ''
with open('day.9.dat') as f:
    for l in f:
        line = line + l.replace('\n', '').replace(' ', '')

length = len(line)
i = 0
out = ''
while i < length:
    if line[i] == '(':
        end = line.find(')', i)
        ele = line[i+1:end].split('x')
        print(ele)
        numchars = int(ele[0])
        times = int(ele[1])
        chars = line[end+1:end+1+numchars]
        print(chars)
        for i in range(times):
            out = out + chars
        i = end + 1 + numchars
    else:
        out = out + line[i]
        i = i + 1

print(out)
print(len(out))
