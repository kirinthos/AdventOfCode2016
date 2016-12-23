#!/usr/bin/env python

import md5

input1 = 'abc'
input2 = 'wtnhxymk'

password = ''
h = '111111111'
mutate = input2
count = 0
for i in range(8):
    while not h[:5] == '00000':
        testString = mutate + str(count)
        h = md5.md5(testString).hexdigest()
        count = count + 1
    password = password + h[5]
    count = count + 1
    h = '1111111111'
print(password)
