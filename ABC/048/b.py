# -*- coding: utf-8 -*-

def f(n, x):
    if n == -1:
        return 0
    return n // x + 1

a, b, x = map(int, input().split())

print(f(b, x) - f(a - 1, x))
