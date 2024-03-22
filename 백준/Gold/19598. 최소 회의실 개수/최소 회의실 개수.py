import heapq

N = int(input())
times = []

# 모든 회의 시간을 입력 받아 리스트에 저장
for _ in range(N):
    start, end = map(int, input().split())
    times.append((start, end))

# 리스트에 저장된 회의 시간들을 시작 시간 기준으로 정렬
times.sort()

# 최소 힙 초기화 및 첫 회의의 끝나는 시간 추가
heap = []
heapq.heappush(heap, times[0][1])

# 각 회의에 대하여 최소 힙을 업데이트
for i in range(1, N):
    if times[i][0] >= heap[0]:  # 현재 회의가 시작할 수 있다면
        heapq.heappop(heap)  # 가장 먼저 끝나는 회의실에서 회의를 진행
    heapq.heappush(heap, times[i][1])  # 현재 회의의 끝나는 시간을 힙에 추가

# 필요한 최소 회의실 개수 출력
print(len(heap))
