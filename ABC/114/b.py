# -*- coding: utf-8 -*-

# input
S = input()

# solve
ans = abs(int(S) - 753)
for i in range(len(S) - 2):
    ans = min(ans, abs(int(S[i:i + 3]) - 753))

# output
print(ans)
