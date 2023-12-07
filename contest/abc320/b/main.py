S = input()
ans = 1
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        T = S[i:j]
        if T == T[::-1]:
            ans = max(ans, len(T))
print(ans)