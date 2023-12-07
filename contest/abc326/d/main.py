N = int(input())
R = input()
C = input()

grid = [[] * N for _ in range(N)]

grid.replace("", ".")
print(grid)