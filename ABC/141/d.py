# -*- coding: utf-8 -*-
import heapq

# input
N, M = map(int, input().split())
A = list(map(int, input().split()))

# solve
ans = [-a for a in A]
heapq.heapify(ans)
for i in range(M):
    tmp = heapq.heappop(ans) * (-1) // 2
    heapq.heappush(ans, tmp * (-1))
ans = [-a for a in ans]

# output
print(sum(ans))
