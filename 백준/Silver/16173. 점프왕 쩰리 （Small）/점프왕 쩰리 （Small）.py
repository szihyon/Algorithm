n = int(input())
visit = [[0]*n for _ in range(n)]

# graph=[list(map(int,input().split())) for _ in range(N)]
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))


flag = 0
def dfs(y, x):
    global flag
    if y < 0 or x < 0 or y > n-1 or x > n-1: return
    if visit[y][x] == 1: return

    if y == n-1 and x == n-1:
        flag = 1
        return

    visit[y][x] = 1

    dfs(y+lst[y][x], x)
    dfs(y, x+lst[y][x])

dfs(0, 0)

if flag == 1:
    print("HaruHaru")
else:
    print("Hing")
