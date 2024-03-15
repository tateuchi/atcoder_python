import sys
def i():
    return int(sys.stdin.readline())
def mi():
    return map(int, sys.stdin.readline().split())
def li():
    return list(map(int, sys.stdin.readline().split()))
def s():
    return sys.stdin.readline().strip()
def ls(n):
    return [list(sys.stdin.readline()) for _ in range(n)]

Q=i()
D=dict()
for i in range(Q):
    Query=input().split()
    if Query[0]=="1":
        _,x,y=Query
        y=int(y)
        D[x]=y
    
    if Query[0]=="2":
        _,x=Query
        print(D[x])