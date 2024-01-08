def solution(park, routes):
    answer = []

    # 시작 지점 찾기
    flag = 0
    h = len(park)
    w = len(park[0])
    for i in range(h):
        if flag == 1: break
        for j in range(w):
            if park[i][j] == "S":
                nowY = i
                nowX = j
                flag = 1
                break
    
    # 방향 정보
    directionY = {"E":0, "W":0, "N":-1, "S":1}
    directionX = {"E":1, "W":-1, "N":0, "S":0}

    # 이동
    for i in range(len(routes)):
        flag = 0
        direction, distance = routes[i].split()
        distance = int(distance)
        for i in range(1, distance+1):
            dy = nowY + directionY[direction] * i
            dx = nowX + directionX[direction] * i
            if dy < 0 or dy > h-1 or dx < 0 or dx > w-1: 
                flag = 1
                break
            if park[dy][dx] == "X": 
                flag = 1
                break
        if flag == 1: continue
        nowY = dy
        nowX = dx
    answer = [nowY, nowX]
    return answer