import heapq

def solution(jobs):
    answer = 0
    now = 0
    cnt = 0
    start = -1
    heap = []
    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:   
            current_job = heapq.heappop(heap)
            start = now
            now += current_job[0]
            answer += now - current_job[1] 
            cnt += 1
        else:
            now += 1
    answer = answer // len(jobs)
    return answer 