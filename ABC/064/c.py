# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

color = [0] * 9
for a in A:
    if a < 400:
        color[0] += 1
    elif a < 800:
        color[1] += 1
    elif a < 1200:
        color[2] += 1
    elif a < 1600:
        color[3] += 1
    elif a < 2000:
        color[4] += 1
    elif a < 2400:
        color[5] += 1
    elif a < 2800:
        color[6] += 1
    elif a < 3200:
        color[7] += 1
    else:
        color[8] += 1

ans = 0
for i in range(8):
    if color[i] != 0:
        ans += 1

print('1' if ans == 0 else ans, end=' ')
print(ans + color[8])
