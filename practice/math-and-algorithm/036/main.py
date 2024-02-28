import math

A, B, H, M = map(int, input().split())

Hx = A * math.cos((30 * H + 0.5 * M) * math.pi / 180)
Hy = A * math.sin((30 * H + 0.5 * M) * math.pi / 180)
Mx = B * math.cos((6 * M) * math.pi / 180)
My = B * math.sin((6 * M) * math.pi / 180)

print(math.sqrt((Hx - Mx) ** 2 + (Hy - My) ** 2))