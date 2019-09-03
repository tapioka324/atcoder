# -*- coding: utf-8 -*-

# input
N = int(input())
A = list(map(int, input().split()))

# solve
ans = 0
is_odd = False
while True:
    for i in range(N):
        if A[i] % 2 == 1:
            is_odd = True
    if not is_odd:
        for i in range(N):
            A[i] /= 2
        ans += 1
    else:
        break

# output
print(ans)
