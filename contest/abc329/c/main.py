N = int(input())
S = input()

lengths = {chr(i): 0 for i in range(97, 123)}
count = 0
i = 0
while i < N:
    start = i
    while i < N and S[i] == S[start]:
        i += 1
    length = i - start

    if length > lengths[S[start]]:
        count += length - lengths[S[start]]
        lengths[S[start]] = length

print(count)