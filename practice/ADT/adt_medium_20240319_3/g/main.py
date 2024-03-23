import sys
ri = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(ri())
mi = lambda: map(int, ri().split())
li = lambda: list(map(int, ri().split()))
mia = lambda *t: [f(ri()) for f in t]
bi = lambda n: [li() for _ in range(n)]


sys.setrecursionlimit(500005)

N,K,D=mi()
A=li()

dp=[[-1]*D for _ in range(K+1)]
dp[0][0]=0
for a in A:
  for i in range(K-1, -1, -1):
    for j in range(D):
      if dp[i][j] != -1:
        dp[i+1][(j+a)%D] = max(dp[i+1][(j+a)%D], dp[i][j]+a)

print(dp[K][0])