from sys import stdin

H,W,N=map(int,stdin.readline().split())
Z = [[0]*(W+1) for _ in range(H+1)]
for _ in range(N):
    A,B,C,D=map(int,stdin.readline().split())
    A -= 1
    B -= 1
    Z[A][B] += 1
    Z[C][D] += 1
    Z[A][D] -= 1
    Z[C][B] -= 1

for h in range(H):
    for w in range(W):
        Z[h+1][w] += Z[h][w]
        
for w in range(W):
    for h in range(H):
        Z[h][w+1] += Z[h][w]

for i in range(H):
    print(*Z[i][:W])