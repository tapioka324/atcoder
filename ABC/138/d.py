# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10 ** 7)

# input & solve
input = sys.stdin.readline
N, Q = map(int, input().split())

to = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

ans = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x

def dfs(v, p=-1):
    for u in to[v]:
        if u == p:
            continue
        ans[u] += ans[v]
        dfs(u, v)

dfs(0)

# output
print(*ans)
