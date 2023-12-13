from sys import stdin

N=int(stdin.readline())

G = [[0]*(1509) for _ in range(1509)]

for _ in range(N):
    A,B,C,D=map(int,stdin.readline().split())
    A += 1
    B += 1
    C += 1
    D += 1
    G[A][B] += 1
    G[C][D] += 1
    G[A][D] -= 1
    G[C][B] -= 1

for i in range(1505):
    for j in range(1505):
        G[i][j+1] += G[i][j]

for i in range(1505):
    for j in range(1505):
        G[i+1][j] += G[i][j]

ans = 0
for i in range(1509):
    for j in range(1509):
        if G[i][j] > 0:
            ans += 1

print(ans)