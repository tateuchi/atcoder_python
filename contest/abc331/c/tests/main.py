N = int(input())
A = list(map(int, input().split()))

sort_A = sorted(A)
sum_A = [0]
for a in sort_A:
    sum_A.append(sum_A[-1] + a)

ans = []
for a in A:
    low, high = 0, N
    while low < high:
        mid = (low + high) // 2
        if sort_A[mid] <= a:
            low = mid + 1
        else:
            high = mid
    ans.append(sum_A[N] - sum_A[low])


print(*ans)
