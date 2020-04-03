# -*- coding: utf-8 -*-

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

ans = 0
hands = list()
for t in T:
    if t == 'r':
        hands.append('p')
    elif t == 's':
        hands.append('r')
    else:
        hands.append('s')

for i in range(K, N, K):
    h = ['r', 's', 'p']
    if hands[i - K] == hands[i]:
        h.remove(hands[i])
        hands[i] = h[0]
        if i + K < N and hands[i] == hands[i + K]:
            h.remove(hands[i])
            hands[i] = h[0]

for t, h in zip(T, hands):
    if t == 'r' and h == 'p':
        ans += P
    elif t == 's' and h == 'r':
        ans += R
    elif t == 'p' and h == 's':
        ans += S
    print(ans)

print(T)
print(hands)
print(ans)
