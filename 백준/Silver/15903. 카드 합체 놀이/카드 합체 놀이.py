import heapq
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
for _ in range(m):
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    new_num = num1 + num2
    for _ in range(2):
        heapq.heappush(cards, new_num)
print(sum(cards))