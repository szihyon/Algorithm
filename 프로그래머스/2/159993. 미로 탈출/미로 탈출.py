from collections import deque

def solution(maps):
    answer = 0
    
    #좌표찾기
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                startY = i
                startX = j
            elif maps[i][j] == 'E':
                endY = i
                endX = j
            elif maps[i][j] == 'L':
                leverY = i
                leverX = j
    
    directY = [-1, 0, 0, 1]
    directX = [0, -1, 1, 0]
    flag1 = 0
    #레버찾기(시작점>레버)
    queue = deque([(startY, startX, 0)])
    visit = [[0]*m for _ in range(n)]
    visit[startY][startX] = 1
    while queue:
        nowY, nowX, dist = queue.popleft()
        if nowY==leverY and nowX==leverX:
            flag1 = 1
            answer += dist
            break
        for d in range(4):
            nextY = directY[d] + nowY
            nextX = directX[d] + nowX
            if nextY<0 or nextX<0 or nextY>n-1 or nextX>m-1: continue
            if maps[nextY][nextX] == "X": continue
            if visit[nextY][nextX] == 1: continue
            # if maps[nextY][nextX] == "O" or maps[nextY][nextX] == "L":
            visit[nextY][nextX] = 1
            queue.append((nextY, nextX, dist+1))
    
    flag2 = 0
    #출구찾기(레버>출구)
    queue = deque([(leverY, leverX, 0)])
    visit = [[0]*m for _ in range(n)]
    visit[leverY][leverX] = 1
    while queue:
        nowY, nowX, dist = queue.popleft()
        if nowY==endY and nowX==endX:
            flag2 = 1
            answer += dist
            break
        for d in range(4):
            nextY = directY[d] + nowY
            nextX = directX[d] + nowX
            if nextY<0 or nextX<0 or nextY>n-1 or nextX>m-1: continue
            if maps[nextY][nextX] == "X": continue
            if visit[nextY][nextX] == 1: continue
            # if maps[nextY][nextX] == "O" or maps[nextY][nextX] == "E":
            visit[nextY][nextX] = 1
            queue.append((nextY, nextX, dist+1))

    if flag1==0 or flag2==0:
        answer = -1
                
    return answer