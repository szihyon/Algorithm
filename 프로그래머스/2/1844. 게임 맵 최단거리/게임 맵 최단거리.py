from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    directY = [0, 0, 1, -1]
    directX = [1, -1, 0, 0]
    
    q = deque()
    q.append([0, 0, 1])
    
    while q:
        nowY, nowX, move = q.popleft()
        if nowY == n-1 and nowX == m-1:
            return move
        for i in range(4):
            dy = directY[i] + nowY
            dx = directX[i] + nowX
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1: continue
            if maps[dy][dx] == 0: continue
            maps[dy][dx] = 0
            q.append([dy, dx, move+1])
    
    return -1