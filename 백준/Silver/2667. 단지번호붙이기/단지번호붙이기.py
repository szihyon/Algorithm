from collections import deque

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input())))

def bfs(y, x):
    h_cnt = 0
    lst[y][x] = 0
    directionY = [-1, 0, 0, 1]
    directionX = [0, -1, 1, 0]
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        h_cnt += 1

        for i in range(4):
            dy = directionY[i] + y
            dx = directionX[i] + x
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1: continue
            if lst[dy][dx] == 1:
                lst[dy][dx] = 0
                q.append((dy, dx))

    return h_cnt


t_cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if lst[i][j] ==1:
            t_cnt += 1
            res.append(bfs(i, j))
res.sort()

print(t_cnt)
for i in range(len(res)):
    print(res[i])