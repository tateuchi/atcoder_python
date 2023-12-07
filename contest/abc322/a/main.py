N = int(input())
S = input()

for i in range(2, N):
    if S[i - 2] == "A" and S[i - 1] == "B" and S[i] == "C":
        print(i-1)
        exit()

print(-1)

# S = [input(), input()][1]
# ans = S.find("ABC")
# print(ans + 1 if ans != -1 else -1)
