N = int(input())
slimes = {}

for _ in range(N):
    s, c = map(int, input().split())
    slimes[s] = slimes.get(s, 0) + c

while True:
    merged = False
    for s in sorted(slimes.keys()):
        while slimes[s] > 1:
            merged = True
            count = slimes[s] // 2
            slimes[s] -= count * 2
            slimes[s * 2] = slimes.get(s * 2, 0) + count

    if not merged:
        break

total_slimes = sum(slimes.values())
print(total_slimes)
