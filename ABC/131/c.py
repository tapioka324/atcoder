# -*- coding: utf-8 -*-

A, B, C, D = map(int, input().split())


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def f(n):
    res = n
    res -= n // C
    res -= n // D
    res += n // lcm(C, D)

    return res


ans = f(B) - f(A - 1)

print(ans)
