T = int(input())

directY = [0, 1]
directX = [1, 0]

def abc(y, x, sumV):
    global minV
    
   if sumV > minV:
    return
    
    if y == n-1 and x == n-1:
        if sumV < minV:
            minV = sumV
        return

    for i in range(2):
        dy = directY[i] + y
        dx = directX[i] + x
        if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:continue
        if visit[dy][dx] == 1: continue
        visit[dy][dx] = 1
        abc(dy, dx, sumV+lst[dy][dx])
        visit[dy][dx] = 0

for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    minV = 21e8
    visit = [[0]*n for _ in range(n)]
    visit[0][0] = 1
    abc(0, 0, lst[0][0])
    print(f"#{tc} {minV}")
