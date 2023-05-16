from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
size = 2
cnt = 0


def bfs(stY, stX):
    global size, cnt
    q = deque()
    q.append((stY, stX, 0))
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    visit = [[0] * N for _ in range(N)]
    visit[stY][stX] = 1
    found_fish = []

    while q:
        nowY, nowX, dist = q.popleft()

        if 0 < lst[nowY][nowX] < size:
            found_fish.append((dist, nowY, nowX))

        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
            if visit[dy][dx] == 1: continue
            if lst[dy][dx] > size: continue
            visit[dy][dx] = 1
            q.append((dy, dx, dist + 1))

    if not found_fish:
        return None
    found_fish.sort()

    return found_fish[0]


def eat_fish():
    global size, cnt
    sharkY, sharkX = 0, 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 9:
                sharkY, sharkX = i, j
                lst[i][j] = 0

    total = 0
    while True:
        result = bfs(sharkY, sharkX)
        if result is None:
            return total

        dist, fishY, fishX = result
        total += dist
        lst[fishY][fishX] = 0
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
        sharkY, sharkX = fishY, fishX


print(eat_fish())