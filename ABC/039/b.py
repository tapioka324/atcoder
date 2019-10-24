# -*- coding: utf-8 -*-

# input
X = int(input())

# solve
for i in range(1, 200):
    if i ** 4 == X:
        ans = i
        break

# output
print(ans)
