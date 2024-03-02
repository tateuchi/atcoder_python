import sys
def I():
    return int(sys.stdin.readline())
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

for i in range(M):
    A,B=mi()
    G[A-1].append(B)
    G[B-1].append(A)

for i in range(N):
    print(f"{i+1}: ",end="")
    print("{",end="")
    for j in range(len(G[i])):
        if j != len(G[i])-1:
            print(f"{G[i][j]},",end=" ")
        else:
            print(f"{G[i][j]}",end="")

    print("}")

