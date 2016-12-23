#!/usr/bin/python

class Bot:
    def __init__(self):
        self.low = None
        self.high = None

    def receive(self, value):
        if self.low != None and self.high != None:
            print('BIG ERROR MAN')
        elif self.low != None and value < self.low:
            self.high = self.low
            self.low = value
        elif self.high != None and value > self.high:
            self.low = self.high
            self.high = value
        elif self.low == None:
            self.low = value
        else:
            self.high = value

    def giveLow(self):
        tmp = self.low
        self.low = None
        return tmp

    def giveHigh(self):
        tmp = self.high
        self.high = None
        return tmp

    def isValid(self):
        return self.low != None and self.high != None

def printSystem():
    for b in bots:
        bot = bots[b]
        print('bot ' + str(b) + ': (' + str(bot.low) + ', ' + str(bot.high) + ')')
    for o in outputs:
        out = outputs[o]
        print('output ' + str(o) + ': ' + str(out))


bots = dict()
outputs = dict()
comparisonBot = None

starts = []
instructions = []
with open('day.10.dat') as f:
    for line in f:
        line = line.replace('\n', '')
        split = line.split(' ')
        if split[0] == 'value':
            starts.append(line)
        else:
            instructions.append(line.split(' '))


for s in starts:
    split = s.split(' ')
    botnumber = int(split[-1])
    b = None
    if botnumber in bots:
        b = bots[botnumber]
    else:
        b = Bot()
        bots[botnumber] = b
    b.receive(int(split[1]))

printSystem()
print()
print()

while len(instructions) > 0:
    i = 0
    while i < len(instructions):
        cur = instructions[i]
        botnumber = int(cur[1])
        if not botnumber in bots:
            i = i + 1
            continue

        b = bots[botnumber]
        if b.isValid(): # perform the instruction
            lowtarget = cur[5]
            lownumber = int(cur[6])
            hightarget = cur[-2]
            highnumber = int(cur[-1])

            if b.low == 17 and b.high == 61:
                comparisonBot = botnumber

            if lowtarget == 'output':
                if lownumber in outputs:
                    outputs[lownumber].append(b.giveLow())
                else:
                    outputs[lownumber] = [b.giveLow()]
            else:
                if not lownumber in bots:
                    bots[lownumber] = Bot()
                bots[lownumber].receive(b.giveLow())

            if hightarget == 'output':
                if highnumber in outputs:
                    outputs[highnumber].append(b.giveHigh())
                else:
                    outputs[highnumber] = [b.giveHigh()]
            else:
                if not highnumber in bots:
                    bots[highnumber] = Bot()
                bots[highnumber].receive(b.giveHigh())
            break
        else:
            i = i + 1
    instructions.pop(i)

printSystem()
if comparisonBot != None:
    print('comparison bot: ' + str(comparisonBot))
else:
    print('no comparison bot found')
print(outputs[0][0] * outputs[1][0] * outputs[2][0])
