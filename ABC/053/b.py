# -*- coding: utf-8 -*-

# input
s = input()

# solve
for i in range(len(s)):
    if s[i] == 'A':
        a = i
        break

for i in reversed(range(len(s))):
    if s[i] == 'Z':
        z = i
        break

# output
print(z - a + 1)
