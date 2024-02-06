n, m = map(int, input().split())
lst = []
cnt = 0

for _ in range(n):
    lst.append(list(input()))

# 가로 탐색
for i in range(n):
    flag = 0
    for j in range(m):
        if lst[i][j] == "-":
            if flag == 0:
                flag = 1
                cnt += 1
        else:
            flag = 0

# 세로 탐색
for i in range(m):
    flag = 0
    for j in range(n):
        if lst[j][i] == "|":
            if flag == 0:
                flag = 1
                cnt += 1
        else:
            flag = 0

print(cnt)