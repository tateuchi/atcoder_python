S=input()

if S[0].upper():
    for i in range(1, len(S)):
        if S[i].isupper():
            print("No")
            exit()
    print("Yes")
else:
    print("No")