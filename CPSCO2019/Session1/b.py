S = input()

ans = list()
for i in set(S):
    ans.append(S.count(i))

print('Yes' if len(set(ans)) == 1 else 'No')
