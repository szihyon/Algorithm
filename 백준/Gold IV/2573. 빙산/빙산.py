from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

directY = [-1, 1, 0, 0]
directX = [0, 0, -1, 1]

def count_icebergs(y, x):
    q = deque()
    q.append([y, x])
    while q:
        nowY, nowX = q.popleft()
        for i in range(4):
            dy = nowY + directY[i]
            dx = nowX + directX[i]
            if dy < 0 or dx < 0 or dy > n - 1 or dx > m - 1: continue
            if maps[dy][dx] == 0: continue
            if visit[dy][dx] == 1: continue
            visit[dy][dx] = 1
            q.append([dy, dx])

year = 0
while True:
    # 1. 현재 빙산 덩어리 개수 확인
    num_icebergs = 0
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and visit[i][j] == 0:
                visit[i][j] = 1
                count_icebergs(i, j)
                num_icebergs += 1

    # 2. 빙산 덩어리가 2개 이상이면 날짜 출력 후 종료
    if num_icebergs >= 2:
        print(year)
        break

    # 3. 빙산 덩어리가 1개인 경우 각 위치에서 얼만큼 녹아야 하는지 계산
    elif num_icebergs == 1:
        melt_cnt_lst = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if maps[i][j] != 0:
                    melt_cnt = 0
                    for k in range(4):
                        dy = i + directY[k]
                        dx = j + directX[k]
                        if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
                        if maps[dy][dx] == 0:
                            melt_cnt += 1
                    melt_cnt_lst[i][j] = melt_cnt

        # 4. 얼만큼 녹아야 하는지 계산된 값을 바탕으로 빙산 녹이기
        for i in range(n):
            for j in range(m):
                if maps[i][j] != 0:
                    maps[i][j] = maps[i][j] - melt_cnt_lst[i][j]
                    if maps[i][j] < 0:
                        maps[i][j] = 0
        year += 1

    # 5. 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력
    elif num_icebergs == 0:
        print(0)
        break
