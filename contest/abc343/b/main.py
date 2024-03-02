import sys
def I():
    return int(sys.stdin.readline())
def MI():
    return map(int, sys.stdin.readline().split())
def LI():
    return list(map(int, sys.stdin.readline().split()))

N=I()
A=[LI() for _ in range(N)]
G=[[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            G[i].append(j+1)

for g in G:
    print(*g)
