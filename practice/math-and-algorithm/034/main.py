import math

N = int(input())
x, y = [], []

for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

ans = 10 ** 9

for i in range(N):
    for j in range(i+1, N):
        dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
        ans = min(ans, dist)

print(ans)