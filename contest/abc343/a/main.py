import sys
def I():
    return int(sys.stdin.readline())
def MI():
    return map(int, sys.stdin.readline().split())
def LI():
    return list(map(int, sys.stdin.readline().split()))

A,B=MI()

for i in range(0,10):
    if i != A + B:
        print(i)
        exit()