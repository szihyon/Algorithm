N, M = map(int, input().split())

answer = 0
lst = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a-1][b-1] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if lst[j][i] == 1 and lst[i][k] == 1:
                lst[j][k] = 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][j] == 1 or lst[j][i] == 1:
            cnt += 1
    if cnt == N-1:
        answer += 1

print(answer)