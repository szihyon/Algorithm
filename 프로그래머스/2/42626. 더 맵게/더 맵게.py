import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1 and scoville[0] < K:
        f1 = heapq.heappop(scoville)
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville, f1 + (f2 * 2))
        cnt += 1
    return cnt if scoville[0] >= K else -1