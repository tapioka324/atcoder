S = input()
K = int(input())

m = K % len(S)
print(S[m:] + S[0:m])
