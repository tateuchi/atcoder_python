import math

D = int(input())

x = 0
ans = D

if int(math.sqrt(D))**2 == D:
    ans = 0
else:
    while x*x <= D:
        y = int(math.sqrt(D - x * x))
        for delta in [-1, 0, 1]:
            y_adj = max(0, y + delta)
            current_diff = abs(x * x + y_adj * y_adj - D)
            ans = min(ans, current_diff)
        if ans == 0:
            break
        x += 1

print(ans)
