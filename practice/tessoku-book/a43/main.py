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

N,L=mi()
AB=[]
for _ in range(N):
    a,b=input().split()
    AB.append((int(a),b))

ans = 0
for i in range(N):
    if AB[i][1] == "E":
        ans = max(ans, L - AB[i][0])

    if AB[i][1] == "W":
        ans = max(ans, AB[i][0])

print(ans)