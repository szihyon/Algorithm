N = int(input())
arr = [[0]*N for _ in range(N)]
findNum = int(input())
nowY = nowX = N // 2
arr[nowY][nowX] = 1

# 상,우,하,좌 순서
directY = [-1, 0, 1, 0]
directX = [0, 1, 0, -1]
dir = 0
move = 1

num = 2
# 1, 1, 2, 2, 3, 3, 4, 4 .... 번씩 이동
while num <= N*N:
    for _ in range(2):
        if num > N*N:  
            break
        for _ in range(move):
            dy = nowY + directY[dir]
            dx = nowX + directX[dir]
            if 0 <= dy < N and 0 <= dx < N:
                arr[dy][dx] = num
                nowY = dy
                nowX = dx
            num += 1
        dir = (dir + 1) % 4
    move += 1

ansY = ansX = 0
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
        if arr[i][j] == findNum:
            ansY = i
            ansX = j
    print()

print(ansY+1, ansX+1)
