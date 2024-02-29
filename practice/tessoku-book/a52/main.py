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

from collections import deque

Q=i()
D=deque()
for i in range(Q):
    
    Query=list(input().split())

    if Query[0] == "1":
        D.append(Query[1])

    if Query[0] == "2":
        print(D[0])

    if Query[0] == "3":
        D.popleft()