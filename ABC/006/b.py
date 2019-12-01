# -*- coding: utf-8 -*-

n = int(input())

l = [0] * 1000010
l[2] = 1

for i in range(3, n):
    l[i] = (l[i - 1] + l[i - 2] + l[i - 3]) % 10007

print(l[n - 1])
