# 1: 흑돌(B)
# 2: 백돌(W)

def game(y, x, stone):
    directionY = [-1, -1, -1, 0, 0, 1, 1, 1]
    directionX = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(len(directionY)):
        temp =[]
        for j in range(1, n):
            dy = directionY[i]*j + y
            dx = directionX[i]*j + x
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:continue
            if stone == 1:
                if lst[dy][dx] == 2:    # 다른색 돌을 만나면 일단 temp리스트에 저장
                    temp.append((dy,dx))
                elif lst[dy][dx] == 1:  # 같은 색 돌을 만났는데
                    if len(temp) == 0:  # 만약 temp가 비어있다면
                        break
                    else:    # 만약 temp에 요소가 있다면
                        lst[y][x] = 1   # 일단 처음 입력받은 좌표에 돌을 놓고
                        for i in range(len(temp)):  # temp에 있는 좌표값대로 전부 변경
                            k, g = temp[i]
                            lst[k][g] = 1
                        break
                elif lst[dy][dx] == 0:
                    break

            elif stone == 2:
                if lst[dy][dx] == 1:
                    temp.append((dy, dx))
                elif lst[dy][dx] == 2:
                    if len(temp) == 0:
                        break
                    else:
                        lst[y][x] = 2
                        for i in range(len(temp)):
                            k, g = temp[i]
                            lst[k][g] = 2
                        break
                elif lst[dy][dx] == 0:
                    break
    return

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = [[0]*n for _ in range(n)]
    lst[n//2-1][n//2-1] = 2
    lst[n//2-1][n//2] = 1
    lst[n//2][n//2-1] = 1
    lst[n//2][n//2] = 2
    cnt = 0
    for i in range(m):
        x, y, stone = map(int, input().split())
        if cnt == n * n - 4:
            break
        game(y-1, x-1, stone)
        cnt += 1
        # print(lst)
    B = 0
    W = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 1:
                B += 1
            if lst[i][j] == 2:
                W += 1
    print(f"#{tc} {B} {W}")
