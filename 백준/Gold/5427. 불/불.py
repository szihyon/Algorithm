from collections import deque

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    graph = []
    for _ in range(h):
        graph.append(list(input()))

    #배열 4개 사용- fire,fire_time / person,visit
    fire = deque([])
    fire_time = [[-1]*w for _ in range(h)]  # 불 번지는 시간을 별도 배열에 저장
    
    person = deque([])
    visit = [[-1]*w for _ in range(h)]
    
    #불, 시작 위치 
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                # graph[i][j] = '.'
                person.append((i, j, 0))
                visit[i][j] = 1 #시작 위치 방문체크
            elif graph[i][j] == '*':
                fire.append((i, j, 0))
                fire_time[i][j] = 0 #처음 불이 있는 위치 시간 저장

    # 방향배열
    directY = [-1, 1, 0, 0]
    directX = [0, 0, -1, 1]

    #불 번지는 BFS 
    while fire:
        nowY, nowX, time = fire.popleft()
        for d in range(4):
            nextY = nowY + directY[d]
            nextX = nowX + directX[d]
            if nextY<0 or nextX<0 or nextY>h-1 or nextX>w-1: continue #범위 벗어나는 경우
            if graph[nextY][nextX] == '#': continue #벽은 불이 붙지 않음
            if fire_time[nextY][nextX] == -1: #아직 불이 붙지 않은 경우
                fire_time[nextY][nextX] = time + 1
                fire.append((nextY, nextX, time+1))
    
    #사람 이동 BFS 
    answer = 'IMPOSSIBLE'
    found = False
    while person and not found:
        nowY, nowX, time = person.popleft()
        # if nowY==0 or nowX==0 or nowY==h-1 or nowX==w-1: #가장자리에 있는 경우 탈출 가능
        #     answer = time+1 
        #     break
        for d in range(4):
            nextY = nowY + directY[d]
            nextX = nowX + directX[d]
            # '범위를 벗어나면' 탈출 성공
            if nextY<0 or nextX<0 or nextY>h-1 or nextX>w-1: 
                answer = time+1
                found = True
                break
            if graph[nextY][nextX] == '#': continue #벽은 이동 불가
            if visit[nextY][nextX] == True: continue #방문했던 곳은 이동 안함
            if fire_time[nextY][nextX] == -1 or time+1 < fire_time[nextY][nextX]: #불이 아예 안 오거나(fire_time == -1) 조건 추가
            # if time+1 < fire_time[nextY][nextX]: #다음칸 이동 시에도 불이 없는 경우 이동
                visit[nextY][nextX] = True
                person.append((nextY, nextX, time+1))
    
    print(answer)