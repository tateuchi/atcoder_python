x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if d < abs(r1 - r2):
    print(1)
elif d == abs(r1 - r2):
    print(2)
elif abs(r1 - r2) < d < abs(r1 + r2):
    print(3)
elif d == abs(r1 + r2):
    print(4)
else:
    print(5)