# -*- coding: utf-8 -*-

# input
A = int(input())
B = int(input())
C = int(input())

# solve
ans = [A, B, C]
ans.sort(reverse=True)

# output
print(ans.index(A) + 1)
print(ans.index(B) + 1)
print(ans.index(C) + 1)
