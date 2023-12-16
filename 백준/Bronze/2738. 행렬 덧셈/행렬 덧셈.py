n, m = map(int, input().split())
lstA = []
lstB = []
lstC = [[0]*m for _ in range(n)]

# 행렬A
for i in range(n):
    lstA.append(list(map(int, input().split())))

# 행렬B
for i in range(n):
    lstB.append(list(map(int, input().split())))

# 행렬C = 행렬A + 행렬B
for i in range(n):
    for j in range(m):
        lstC[i][j] = lstA[i][j] + lstB[i][j]

# 행렬C 출력
for i in range(n):
    for j in range(m):
        print(lstC[i][j], end=" ")
    print()