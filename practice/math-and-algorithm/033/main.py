import math

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

BAx, BAy = ax - bx, ay - by
BCx, BCy = cx - bx, cy - by

CAx, CAy = ax - cx, ay - cy
cbx, cby = bx - cx, by - cy

p = 2
if BAx * BCx + BAy * BCy < 0:
    p = 1
if CAx * cbx + CAy * cby < 0:
    p = 3

if p == 1:
    ans = math.sqrt(BAx ** 2 + BAy ** 2)
elif p == 3:
    ans = math.sqrt(CAx ** 2 + CAy ** 2)
elif p == 2:
    ans = abs(BAx * BCy - BAy * BCx)
    ans /= math.sqrt(BCx ** 2 + BCy ** 2)

print("%.12f" % ans)
