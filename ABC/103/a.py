# -*- coding: utf-8 -*-

# input
A = list(map(int, input().split()))

# solve
A.sort()
ans = 0
for i in range(2):
    ans += abs(A[i + 1] - A[i])

# output
print(ans)
