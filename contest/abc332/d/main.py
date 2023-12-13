from collections import Counter

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

Ca = Counter([item for sublist in A for item in sublist])
Cb = Counter([item for sublist in B for item in sublist])

if Ca != Cb:
    print(-1)
else:
    count = 0
    ansh = 0
    for h in range(H):
        if set(A[h]) != set(B[h]):
            count += 1
    if count % 2 == 0:
        ansh = count//2
    else:
        ansh = count//2 + 1
    transposed_A = [list(col) for col in zip(*A)]
    transposed_B = [list(col) for col in zip(*B)]
    count = 0
    answ = 0
    for w in range(W):
        if set(transposed_A[w]) != set(transposed_B[w]):
            count += 1
    if count % 2 == 0:
        answ = count//2
    else:
        answ = count//2 + 1

    print(ansh*answ)