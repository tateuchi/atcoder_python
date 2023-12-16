N=int(input())
h=list(map(int,input().split()))

dp=[0]*N
dp[1]=abs(h[1]-h[0])
ans = [1]
for i in range(2,N):
    dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))

Place = N
ans = [Place]

while Place > 1:
    if dp[Place-1] == dp[Place-2]+abs(h[Place-1]-h[Place-2]):
        Place -= 1
    else:
        Place -= 2
    ans.append(Place)

print(len(ans))
print(*ans[::-1])
