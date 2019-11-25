# -*- coding: utf-8 -*-

A, B, X = map(int, input().split())

left = 0
right = 10 ** 9 + 1

def check(c):
    return A * c + B * len(str(c))

while right - left > 1:
    center = (left + right) // 2
    if check(center) <= X:
        left = center
    else:
        right = center

print(left)
