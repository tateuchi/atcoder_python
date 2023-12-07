N = int(input())

ans = dict()
for i in range(N):
    S = input()
    count = 0
    for j in range(N):
        if S[j] == "o":
            count += 1
    ans[i] = count

ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)

for i in range(N):
    if i != N-1:
        print(ans[i][0]+1, end=" ")
    else:
        print(ans[i][0]+1)