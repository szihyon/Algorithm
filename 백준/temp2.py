from collections import deque

def bfs(stY, stX):
    q = deque()
    q.append((stY, stX))
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    cnt2 = 0

    while q:
        nowY, nowX = q.popleft()
        lst[nowY][nowX] = 1
        cnt2 += 1
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > m-1 or dx > n-1:continue
            if lst[dy][dx] == 0:
                q.append((dy, dx))

    return cnt2

m, n, k = map(int, input().split())
lst = [[0]*n for _ in range(m)]

cnt = 0
ans = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            lst[i][j] = 1

for i in range(m):
    for j in range(n):
        if lst[i][j] == 0:
            cnt += 1
            area = bfs(i, j)
            ans.append(area)

print(cnt)
print(ans)
