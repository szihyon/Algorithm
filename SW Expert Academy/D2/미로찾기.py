T = int(input())

def check(y, x):
    global flag
    if y == edY and x == edX:
        flag = 1
        return

    for i in range(len(directionY)):
        dy = directionY[i] + y
        dx = directionX[i] + x
        if dy < 0 or dx < 0 or dy > n-1 or dx > n-1: continue
        if lst[dy][dx] == '1' or lst[dy][dx] == "P": continue
        lst[dy][dx] = "P"
        check(dy, dx)
        if flag == 1:
            return

for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(input()))
    for i in range(n):
        for j in range(n):
            if lst[i][j] == '2':
                stY = i
                stX = j
            if lst[i][j] == '3':
                edY = i
                edX = j

    directionY = [-1, 0, 0, 1]
    directionX = [0, -1, 1, 0]
    flag = 0
    lst[stY][stX] = "P"
    check(stY, stX)
    if flag == 1:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
