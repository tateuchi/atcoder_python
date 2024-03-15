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

from bisect import *

Q=i()
Query=[li() for _ in range(Q)]
L=list()
for i in range(Q):
    if Query[i][0]==1:
        _,x=Query[i]
        insort_left(L,x)

    if Query[i][0]==2:
        if len(L) == 0:
            print(-1)
        else:
            _,x=Query[i]
            pos=bisect_left(L,x)
            if pos == len(L):
                ans = abs(x - L[-1])
            else:
                ans = min(abs(x-L[pos]), abs(x-L[pos-1]))
            print(ans)