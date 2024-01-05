def solution(park, routes):
    answer = []
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
    for i in range(len(routes)):
        flag = 0
        direction, distance = routes[i].split()
        distance = int(distance)
        if direction == "E":
            if nowX + distance < 0 or nowX + distance > w-1: continue
            for i in range(1, distance + 1):
                if park[nowY][nowX + i] == "X":
                    flag = 1
                    break
            if flag == 1:
                continue
            nowX += distance
        elif direction == "W":
            if nowX - distance < 0 or nowX - distance > w-1: continue
            for i in range(1, distance + 1):
                if park[nowY][nowX - i] == "X":
                    flag = 1
                    break
            if flag == 1:
                continue
            nowX -= distance
        elif direction == "N":
            if nowY - distance < 0 or nowY - distance > h-1: continue
            for i in range(1, distance + 1):
                if park[nowY - i][nowX] == "X":
                    flag = 1
                    break
            if flag == 1:
                continue
            nowY -= distance
        elif direction == "S":
            if nowY + distance < 0 or nowY + distance > h-1: continue
            for i in range(1, distance + 1):
                if park[nowY + i][nowX] == "X":
                    flag = 1
                    break
            if flag == 1:
                continue
            nowY += distance
    answer = [nowY, nowX]
    return answer