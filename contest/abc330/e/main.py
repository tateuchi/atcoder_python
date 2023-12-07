N, Q =  map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    i, x = map(int, input().split())
    A[i-1] = x

    B = sorted(A)
    if B[0] != 0:
        print(0)
    else:
        ans = B[-1]+1
        for i in range(1, len(B)):
            if B[i] - B[i-1] > 1:
                ans = B[i-1] + 1
        print(ans)