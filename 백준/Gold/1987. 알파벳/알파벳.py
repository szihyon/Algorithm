r, c = map(int, input().split())
lst = [list(input()) for _ in range(r)]
directY = [-1, 0, 0, 1]
directX = [0, -1, 1, 0]
st = [[]]

def dfs(y, x, cnt):
    global M_cnt
    if cnt > M_cnt:
        M_cnt = cnt

    for i in range(4):
        dy = directY[i] + y
        dx = directX[i] + x
        if dy < 0 or dx < 0 or dy > r-1 or dx > c-1: continue
        if visited[ord(lst[dy][dx])] == 1: continue
        visited[ord(lst[dy][dx])] = 1
        dfs(dy, dx, cnt+1)
        visited[ord(lst[dy][dx])] = 0


visited = [0]*100
visited[ord(lst[0][0])] = 1
M_cnt = 0

dfs(0, 0, 1)
print(M_cnt)