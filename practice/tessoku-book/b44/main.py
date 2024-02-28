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

N=i()
A=[li() for _ in range(N)]
T=[i for i in range(N)]

Q=i()
for i in range(Q):
    Query=li()
    if Query[0] == 1:
        _,x,y=Query
        T[x-1], T[y-1] = T[y-1], T[x-1]
    
    if Query[0] == 2:
        _,x,y=Query
        print(A[T[x-1]][y-1])