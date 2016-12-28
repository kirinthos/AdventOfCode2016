#!/usr/bin/env python

totalSum = 0

realRooms = []
with open('day.4.dat') as f:
    for line in f:
        bracket = line.find('[')
        name = line[:bracket]
        code = line[bracket+1:bracket+6]
        sectorDash = name.rfind('-')
        sectorID = name[sectorDash+1:]
        name = name[:sectorDash]

        chars = dict()
        for c in name:
            if c != '-':
                if c in chars:
                    chars[c] = chars[c] + 1
                else:
                    chars[c] = 1

        repeats = [ (k, v) for k, v in chars.items() ]
        def sortFunc(a, b):
            if a[1] > b[1]:
                return -1
            elif a[1] < b[1]:
                return 1
            else:
                if a[0] < b[0]:
                    return -1
                else:
                    return 1

        repeats.sort(sortFunc)
        genCode = ''.join([x[0] for x in repeats[:5]])
        if genCode == code:
            totalSum = totalSum + int(sectorID)
            unencrypt = ''
            aord = ord('a')
            for c in name:
                unencrypt = unencrypt + chr(((ord(c) - aord + int(sectorID)) % 26) + aord)
            realRooms.append(unencrypt + '-' + sectorID)

print(totalSum)
print(realRooms)
i = 0
for r in realRooms:
    if 'north' in r:
        print(r, i)
    i = i + 1
