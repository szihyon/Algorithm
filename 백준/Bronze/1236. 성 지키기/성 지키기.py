n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]
height = 0
width = 0

for i in range(n):
    cnt = 0
    for j in range(m):
        if lst[i][j] == "X":
            cnt += 1
    if cnt == 0:
        height += 1

for i in range(m):
    cnt = 0
    for j in range(n):
        if lst[j][i] == "X":
            cnt += 1
    if cnt == 0:
        width += 1

ans = 0
ans += min(height, width)
ans += (max(height, width) - min(height, width))
print(ans)