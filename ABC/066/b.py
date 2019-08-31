# -*- coding: utf-8 -*-

# input
S = input()

# solve
for i in range(len(S)):
    S = S[:-1]
    if len(S) % 2 == 0 and S[:int(len(S)/2)] == S[int(len(S)/2):]:
        break

# output
print(len(S))
