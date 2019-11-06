# -*- coding: utf-8 -*-

# input
N = int(input())

# solve & output
ans = int(N / 2)
if N % 2 == 0:
    print(ans)
else:
    print(ans + 1)
    print('1')
for i in range(ans):
    print('2')
