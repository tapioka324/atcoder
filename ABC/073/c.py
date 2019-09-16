# -*- coding: utf-8 -*-

# input
N = int(input())
A = list()
for _ in range(N):
    A.append(int(input()))

# solve
ans = set()
for i in range(N):
    if A[i] in ans:
        ans.remove(A[i])
    else:
        ans.add(A[i])

# output
print(len(ans))
