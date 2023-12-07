M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d == D:
  d = 0
  m += 1

d += 1

if m > M:
  y += 1
  m = m - M

print(y, m, d)