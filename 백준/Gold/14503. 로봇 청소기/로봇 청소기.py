from collections import deque

n, m = map(int, input().split())
y, x, d = map(int, input().split())

lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 1:
            lst[i][j] = 2


def bfs(y, x, d):
    q = deque()
    q.append((y,x))

    directY = [-1, 0, 1, 0]
    directX = [0, 1, 0, -1]
    back = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    total = 0
    while q:
        nowy, nowx = q.popleft()
        if lst[nowy][nowx] == 0:
            total += 1
            lst[nowy][nowx] = 1
        cnt = 0
        for i in range(4):
            dy = directY[i] + nowy
            dx = directX[i] + nowx
            if 1 <= dy <= n-2 and 1 <= dx <= m-2:
                if lst[dy][dx] == 0:
                    cnt += 1
        # 청소되지 않은(0) 빈 칸이 없는 경우
        if cnt == 0:
            dy = nowy + back[d][0]
            dx = nowx + back[d][1]
            # if dy < 1 or dx < 1 or dy > n-2 or dx > m-2: return total
            if lst[dy][dx] == 2: return total
            q.append((dy,dx))
        # 청소되지 않은 빈 칸이 있는 경우
        else:
            flag = 0
            while flag == 0:
                d = d-1
                if d < 0:
                    d += 4
                dy = nowy + directY[d]
                dx = nowx + directX[d]
                if 1 <= dy <= n-2 and 1 <= dx <= m-2:
                    if lst[dy][dx] == 0:
                        flag = 1
                        q.append((dy, dx))

    return total

print(bfs(y,x,d))