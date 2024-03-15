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

S=s()
d=deque()
for i in range(len(S)):
    if S[i] == "(":
        d.append(i+1)
    
    if S[i] == ")":
        print(d.pop(), i + 1)
