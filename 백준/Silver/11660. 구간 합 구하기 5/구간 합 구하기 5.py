import sys
input = sys.stdin.readline

# 배열 입력값 받기
N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

# 누적합 미리 구하기
sum_lst = [[0]*(N+1) for _ in range(N+1)]
# (1) 첫 번째 행, 열 누적합 채우기
temp1 = temp2 = 0
for i in range(N):
    # 첫 번째 행
    temp1 += lst[0][i]
    sum_lst[0][i] = temp1
    # 첫 번째 열
    temp2 += lst[i][0]
    sum_lst[i][0] = temp2
# 기존 누적합 활용하여 채우기
for i in range(1, N):
    for j in range(1, N):
        # 새로운 숫자 + 이전행까지 누적합 + 이전열까지 누적합 - 중복 영역
        sum_lst[i][j] = lst[i][j] + sum_lst[i-1][j] + sum_lst[i][j-1] - sum_lst[i-1][j-1]

# 좌표 입력 값 받기
for i in range(M):
    answer = 0
    # y1, x1, y2, x2 = list(map(int, input().split()))
    y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())
    answer = sum_lst[y2][x2] - sum_lst[y1-1][x2] - sum_lst[y2][x1-1] + sum_lst[y1-1][x1-1]
    print(answer)

