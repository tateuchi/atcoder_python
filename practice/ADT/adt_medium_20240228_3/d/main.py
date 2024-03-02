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

N=I()
A=[input() for _ in range(N)]

ans = True
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if A[i][j] == "W" and A[j][i] == "L":
                continue
            elif A[i][j] == "L" and A[j][i] == "W":
                continue
            elif A[i][j] == "D" and A[j][i] == "D":
                continue
            else:
                ans = False
                break
    if not ans:
        break

print("correct" if ans else "incorrect")