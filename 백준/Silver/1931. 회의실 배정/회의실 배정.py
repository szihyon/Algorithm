N = int(input())
times = []
for _ in range(N):
    start, end = map(int, input().split())
    times.append([start, end])

# 강의 끝나는 시간이 빠른 순으로 정렬
# times.sort(key=lambda x:x[1])
times.sort(key=lambda x:[x[1],x[0]])

answer = 1
now = times[0][1] # 가장 빨리 끝나는 강의를 먼저 선택
for i in range(1, N):
    if times[i][0] >= now: # 그 다음으로 빨리 끝나는 강의의 시작시간이 이전 강의가 끝나는 시간보다 크거나 같다면
        now = times[i][1] # 강의 선택 후, 해당 강의 끝나는 시간을 현재로 변경
        answer += 1 # 강의 개수 + 1

print(answer)