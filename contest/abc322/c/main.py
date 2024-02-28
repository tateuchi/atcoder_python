N, M = map(int, input().split())
A = list(map(int, input().split()))

day = 1
idx = 0
count = 0
for day in range(1, N+1):
    count = A[idx] - day
    print(count)
    if count == 0:
        idx += 1

# import bisect

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# for i in range(1, N + 1):
#     print(A[bisect.bisect_left(A, i)] - i)
