# -*- coding: utf-8 -*-

# input
a = int(input())
b = int(input())
n = int(input())

# solve
ans = n
while ans % a != 0 or ans % b != 0:
    ans += 1

# output
print(ans)
