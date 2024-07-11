N = int(input())

answer = 2000   # 가장 빠른 시간을 최대값으로 초기화
cnt = 0
for _ in range(N):
    A, B = map(int, input().split())
    if A < B:   # 도착 후 빵이 들어오는 경우
        time = A + (B - A)  # 이동시간 + 대기시간
    elif A == B:    # 도착할 때 빵이 들어오는 경우
        time = A    # 이동시간
    else:   # 도착 전에 빵이 들어오는 경우
        time = A    # 이동시간
        cnt += 1    # 빵을 구할 수 없는 경우 카운트

    if time < answer:   
        answer = time   # 가장 빨리 구할 수 있는 시간 갱신 

if cnt == N:    # N개의 가게 모두 빵을 구할 수 없는 경우
    answer = -1

print(answer)