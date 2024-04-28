import heapq

N = int(input())
candid = []
dasom = int(input())
for _ in range(N-1):
    heapq.heappush(candid, -int(input()))

cnt = 0
while candid and dasom <= -candid[0]:
    candid[0] += 1
    dasom += 1
    cnt += 1
    heapq.heapify(candid)

print(cnt)