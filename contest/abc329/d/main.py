N, M = map(int, input().split())
A = list(map(int, input().split()))

candidate = [0] * (N)
voted = 0
top = 1
for i in range(M):
    candidate[A[i]-1] += 1
    if candidate[A[i]-1] > voted:
        top = A[i]
        voted = candidate[A[i]-1]
    elif candidate[A[i]-1] == voted and top > A[i]:
        top = A[i]
    print(top)
