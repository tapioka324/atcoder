# -*- coding: utf-8 -*-

N = int(input())
H = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * N

dp[0] = 0
for i in range(1, N):
    dp[i] = min(dp[i], dp[i - 1] + abs(H[i] - H[i - 1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i - 2] + abs(H[i] - H[i - 2]))

print(dp[-1])
