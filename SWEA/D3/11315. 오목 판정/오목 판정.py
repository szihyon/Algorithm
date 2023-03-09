def check(y, x):
    directY = [-1, -1, -1, 0, 0, 1, 1, 1]
    directX = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(len(directX)):
        cnt = 1
        for j in range(1, n):
            dy = directY[i] * j + y
            dx = directX[i] * j + x
            if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1: continue
            if lst[dy][dx] == 'o':
                cnt += 1
            elif lst[dy][dx] == '.':
                cnt = 0
            if cnt == 5:
                return True
    return False

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(input()))
    flag = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 'o':
                if check(i, j):
                    flag = 1
                    break
        if flag == 1:
            break
    if flag:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
