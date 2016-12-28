#!/usr/bin/env python

def findIPPair(a):
    l = len(a)
    for i in range(l - 3):
        sub = a[i:i+4]
        if sub[0] != sub[1] and sub[1] == sub[2] and sub[0] == sub[3]:
            return True
    return False

def extractHypernets(a):
    remaining = a
    mainnets = []
    hypernets = []
    start = a.find('[')
    end = a.find(']')
    while start != -1:
        hypernets.append(remaining[start + 1:end])
        mainnets.append(remaining[:start])
        remaining = remaining[end + 1:]
        start = remaining.find('[')
        end = remaining.find(']')
    if end < len(a) - 1:
        mainnets.append(remaining[end+1:-1])
    return hypernets, mainnets

count = 0
with open('day.7.dat') as f:
    for line in f:
        hypernets, remain = extractHypernets(line)
        found = False
        for h in hypernets:
            if findIPPair(h):
                found = True
                break
        if found: # hypernet has pattern, not valid TLS
            continue
        for r in remain:
            if findIPPair(r):
                count = count + 1
                break


print(count)
