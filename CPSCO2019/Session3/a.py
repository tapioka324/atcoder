S = input()

ans = ''
for s in S:
    if s == 'O':
        ans += 'A'
    elif s == 'A':
        ans += 'O'
    else:
        ans += s

print(ans)
