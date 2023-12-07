N = input()

flag = True
for i in range(1, len(N)):
    if N[i-1] <= N[i]:
        flag = False
        break

print("Yes" if flag else "No")