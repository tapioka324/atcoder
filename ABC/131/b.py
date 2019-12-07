# -*- coding: utf-8 -*-

N, L = map(int, input().split())

apple = [L + i - 1 for i in range(1, N + 1)]
diff = abs(apple[0])
for i in range(1, N):
    diff = min(diff, abs(apple[i]))

print(sum(apple) - diff if sum(apple) > 0 else sum(apple) + diff)
