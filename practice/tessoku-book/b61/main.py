import sys
def mi():
    return map(int, sys.stdin.readline().split())
def li():
    return list(map(int, sys.stdin.readline().split()))
def s():
    return sys.stdin.readline().strip()
def ls(n):
    return [list(sys.stdin.readline()) for _ in range(n)]

N,M=mi()
G=[[] for _ in range(N)]

for _ in range(M):
    A,B=mi()
    G[A-1].append(B)
    G[B-1].append(A)

ans = 1
tmp = len(G[ans-1])
for i in range(1, N):
    if len(G[i]) > tmp:
        ans = i + 1
        tmp = len(G[i])

print(ans)