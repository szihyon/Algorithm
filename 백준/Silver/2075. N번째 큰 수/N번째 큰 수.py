import heapq
N = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
for _ in range(N-1):
    nums = list(map(int, input().split()))
    for num in nums:
        if heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
print(heap[0])