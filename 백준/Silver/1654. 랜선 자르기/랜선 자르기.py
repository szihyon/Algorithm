import sys

K, N = map(int, input().split())
cables = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(cables) # 길이 시작점과 끝점 정하기

while start <= end:
    mid = (start + end) // 2 
    cnt = 0
    for cable in cables:
        cnt += cable // mid

    if cnt >= N: # 목표 개수보다 많으면
        start = mid + 1 # 길이를 늘려서 개수 줄이기
    else: # 목표 개수보다 적으면
        end = mid - 1 # 길이를 줄여서 개수 늘리기

print(end) # 최대 길이 end 출력