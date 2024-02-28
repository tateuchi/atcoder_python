x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

def func(ax, ay, bx, by):
    return ax * by - ay * bx

ans1 = func(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
ans2 = func(x2 - x1, y2 - y1, x4 - x1, y4 - y1)
ans3 = func(x4 - x3, y4 - y3, x1 - x3, y1 - y3)
ans4 = func(x4 - x3, y4 - y3, x2 - x3, y2 - y3)


if ans1 == 0 and ans2 == 0 and ans3 == 0 and ans4 == 0:
    A = [x1, y1]
    B = [x2, y2]
    C = [x3, y3]
    D = [x4, y4]
    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C
    if max(A, C) <= min(B, D):
        print('Yes')
    else:
        print('No')

else:
    if ans1 * ans2 < 0 and ans3 * ans4 < 0:
        print('Yes')
    else:
        print('No')
