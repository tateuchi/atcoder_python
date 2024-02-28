N,X=map(int,input().split())
A=list(map(int,input().split()))

def func(X, A):
    L = 0
    R = N - 1
    while L <= R:
        M = (L + R) // 2
        if A[M] == X:
            return M
        elif A[M] < X:
            L = M + 1
        else:
            R = M - 1

ans = func(X, A)

print(ans+1)