# -*- coding: utf-8 -*-

N, K = map(int, input().split())

ans = 0
score = 0
for i in range(1, N + 1):
    score = i
    count = 0
    while score < K:
        count += 1
        score *= 2
    ans += 1 / N * ((1 / 2) ** count)

print(ans)
