import bisect

N=int(input())
A=list(map(int,input().split()))
A.sort()
Q=int(input())
for _ in range(Q):
    X=int(input())
    ans = bisect.bisect_left(A,X)
    print(ans)
