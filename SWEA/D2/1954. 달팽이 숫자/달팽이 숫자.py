T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = [[0] * n for _ in range(n)]
    num = 1
    last_num = n * n

    directY = [0, 1, 0, -1]
    directX = [1, 0, -1, 0]
    dir = 0

    x = y = 0
    while num <= last_num:
        lst[y][x] = num
        dy = y + directY[dir]
        dx = x + directX[dir]
        if (dy < 0 or dx < 0 or dy > n-1 or dx > n-1) or lst[dy][dx] != 0:
            dir = (dir + 1) % 4
        y = y + directY[dir]
        x = x + directX[dir]
        num += 1

    print(f"#{tc}")
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()