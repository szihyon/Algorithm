lst = [[0]*101 for _ in range(101)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            lst[i][j] = 1

directY = [-1, 0, 0, 1]
directX = [0, 1, -1, 0]

def count(y, x):
    cnt = 0
    for i in range(4):
        dy = directY[i] + y
        dx = directX[i] + x
        if dy < 0 or dx < 0 or dy > 100 or dx > 100:continue
        if lst[dy][dx] == 0:
            cnt += 1
    return cnt

ans = 0
for i in range(101):
    for j in range(101):
        if lst[i][j]:
            res = count(i, j)
            ans += res

print(ans)