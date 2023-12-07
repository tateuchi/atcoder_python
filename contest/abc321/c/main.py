K = int(input())

count = 0
i = 0
while count < K:
    i += 1
    S = str(i)
    if len(S) == 1:
        count += 1
    else:
        flag = True
        for j in range(1, len(S)):
            if int(S[j - 1]) <= int(S[j]):
                flag = False
                break
        if flag:
            count += 1

print(i)