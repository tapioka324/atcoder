# -*- coding: utf-8 -*-

# input
A, op, B = map(str, input().split())

# solve & output
print(int(A) + int(B) if op == '+' else int(A) - int(B))
