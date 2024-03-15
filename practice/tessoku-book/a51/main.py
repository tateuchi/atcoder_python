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
S = deque()

for _ in range(Q):
    Query=input().split()
    
    if Query[0] == "1":
        S.append(Query[1])

    if Query[0] == "2":
        print(S[-1])

    if Query[0] == "3":
        S.pop()
    