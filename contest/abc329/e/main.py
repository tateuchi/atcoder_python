N, M = map(int, input().split())
S = input()
T = input()

X = ["#"] * N
for i in range(N - M + 1):
    if S[i:i+M] == T:
        X[i:i+M] = list(T)

X = "".join(X)
if X == S:
    print("Yes")
else:
    print("No")