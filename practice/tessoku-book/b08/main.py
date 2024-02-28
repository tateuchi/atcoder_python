from sys import stdin

N=int(stdin.readline())

MAX = 1509

G = [[0]*MAX for _ in range(MAX)]
for _ in range(N):
    x,y=map(int,stdin.readline().split())
    G[x][y] += 1

for i in range(1,MAX-1):
    for j in range(MAX-1):
        G[i][j+1] += G[i][j]

for j in range(1,MAX-1):
    for i in range(MAX-1):
        G[i+1][j] += G[i][j]

Q=int(stdin.readline())
for _ in range(Q):
    a,b,c,d=map(int,stdin.readline().split())
    a -= 1
    b -= 1
    ans = G[c][d] - G[a][d] - G[c][b] + G[a][b]
    print(ans)