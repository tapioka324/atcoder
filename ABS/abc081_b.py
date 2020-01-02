# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

ans = max(A) // 2
for a in A:
    count = 0
    while True:
        if a % 2 == 1 or a == 1:
            break
        a /= 2
        count += 1
    ans = min(ans, count)

print(ans)
