# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
ans = 'Possible' if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0 else 'Impossible'

# output
print(ans)
