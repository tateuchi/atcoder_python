S = input()

for i in range(len(S)):
    if i == len(S) - 1:
        print(S[i])
    else:
        print(S[i], end=" ")