N, K = map(int, input().split())
table = list(input())

answer = 0
for i in range(N):
    if table[i] == "P": # 사람인 경우
        for j in range(-K, K+1): # 주변 햄버거 탐색(왼쪽 제일 먼 곳부터)
            if 0 <= i+j < N and table[i+j] == "H": # 햄버거가 있는 경우
                answer += 1 # 먹은 개수 + 1
                table[i+j] = "_" # 먹은 표시
                break # 탐색 중지

print(answer)