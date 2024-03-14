N, M = map(int, input().split())

answer = 0
# 키 비교 정보를 담을 2차원 배열
lst = [[0]*N for _ in range(N)]

# 키 비교 여부 체크
for _ in range(M):
    a, b = map(int, input().split())
    lst[a-1][b-1] = 1

# 플로이드 워셜 알고리즘 적용
for i in range(N): # 중간지점
    for j in range(N): # 시작지점
        for k in range(N): # 도착지점
            if lst[j][i] == 1 and lst[i][k] == 1:
                lst[j][k] = 1

# 순서를 매길 수 있는 학생 수 계산
for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][j] == 1 or lst[j][i] == 1:
            cnt += 1
    if cnt == N-1:
        answer += 1

print(answer)