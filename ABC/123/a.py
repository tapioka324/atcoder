# -*- coding: utf-8 -*-

# input
l = list()
for _ in range(5):
    l.append(int(input()))
k = int(input())

# solve
ans = True
for i in range(len(l)):
    for j in range(len(l) - i):
        if l[j] - l[i] > k:
            ans = False

# output
print('Yay!' if ans else ':(')
