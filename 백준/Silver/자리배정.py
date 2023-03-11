directY=[-1, 0, 0, 1]
directX=[0, 1, -1, 0]
dir = 0

c, r = map(int, input().split())
total = c*r
k = int(input())
lst = [[0]*c for _ in range(r)]

num = 1
y = r-1
x = 0
while num <= total:
    lst[y][x] = num
    if num == total:
        break
    dy = directY[dir] + y
    dx = directX[dir] + x
    if dy < 0 or dx < 0 or dy > r-1 or dx > c-1:
        dir = (dir+1)%4
        continue
    if lst[dy][dx] != 0:
        dir = (dir+1)%4
        continue
    y = dy
    x = dx
    num += 1

flag = 0
for i in range(r):
    for j in range(c):
        if lst[i][j] == k:
            flag = 1
            ansY = j+1
            ansX = i+1
            break
    if flag == 1:
        break
if flag:
    print(ansY, r-ansX+1)
else:
    print(0)
