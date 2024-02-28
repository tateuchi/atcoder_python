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

N,Q=mi()
A=[i for i in range(1, N+1)]

flag = True
for i in range(Q):
    Query=li()
    if Query[0] == 1:
        _,x,y=Query
        if flag:
            A[x-1] = y
        else:
            A[N-x] = y

    if Query[0] == 2:
        flag = not flag

    if Query[0] == 3:
        _,x=Query
        if flag:
            print(A[x-1])
        else:
            print(A[N-x])
