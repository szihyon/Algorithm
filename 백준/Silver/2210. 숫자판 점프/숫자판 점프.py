n = 5
lst = []
answer = []
for _ in range(5):
    lst.append(input().split())

directY = [-1, 1, 0, 0]
directX = [0, 0, -1, 1]

def dfs(y, x, level, path):
    if level == 6:
        if path not in answer:
            answer.append(path)
        return

    for i in range(4):
        dy = directY[i] + y
        dx = directX[i] + x
        if dy < 0 or dx < 0 or dy > 4 or dx > 4: continue
        dfs(dy, dx, level+1, path+lst[dy][dx])

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, lst[i][j])

print(len(answer))