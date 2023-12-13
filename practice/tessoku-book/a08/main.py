from sys import stdin

H,W=map(int,stdin.readline().split())
X=[list(map(int,stdin.readline().split())) for _ in range(H)]

Z = [[0]*(W+1) for _ in range(H+1)]
for i in range(1, H+1):
    for j in range(W):
        Z[i][j+1] = Z[i][j] + X[i-1][j]

for j in range(1, W+1):
    for i in range(H):
        Z[i+1][j] += Z[i][j]

Q=int(stdin.readline())
for _ in range(Q):
    A,B,C,D=map(int,stdin.readline().split())
    A -= 1
    B -= 1
    ans = Z[C][D] - Z[A][D] - Z[C][B] + Z[A][B]
    print(ans)