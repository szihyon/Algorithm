import heapq

# 강의 수 입력 받기
n = int(input())

# 강의 시간을 저장할 리스트
lectures = []

for _ in range(n):
    start, end = map(int, input().split())
    lectures.append((start, end))

# 시작 시간 기준으로 강의를 정렬
lectures.sort()

# 강의실의 마지막 강의 종료 시간을 관리할 우선순위 큐
rooms = []

# 첫 번째 강의를 우선순위 큐에 추가
heapq.heappush(rooms, lectures[0][1])

# 나머지 강의들에 대해
for i in range(1, n):
    start, end = lectures[i]
    # 현재 강의의 시작 시간이 강의실에서 제일 먼저 끝나는 강의의 종료 시간보다 크거나 같으면
    # 해당 강의실에서 이어서 강의를 진행할 수 있다.
    if rooms[0] <= start:
        heapq.heappop(rooms)

    # 현재 강의의 종료 시간을 힙에 추가
    heapq.heappush(rooms, end)

# 강의실의 수 출력
print(len(rooms))
