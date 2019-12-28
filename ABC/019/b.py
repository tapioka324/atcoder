# -*- coding: utf-8 -*-

s = input()

now = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] is now:
        count += 1
    else:
        print(now, count, sep='', end='')
        now = s[i]
        count = 1
print(now, count, sep='')
