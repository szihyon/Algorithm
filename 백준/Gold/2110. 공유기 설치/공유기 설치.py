N, C = map(int, input().split())
houses = []
for _ in range(N):
    x = int(input())
    houses.append(x)
houses.sort()

minDist = 1
maxDist = houses[-1] - houses[0]

while minDist <= maxDist:
    mid = (minDist + maxDist) // 2
    wifi = [0]
    cnt = 1
    for i in range(1, len(houses)):
        if houses[i] - houses[wifi[-1]] >= mid:
            wifi.append(i)
            cnt += 1
    if cnt >= C:
        minDist = mid + 1
    else:
        maxDist = mid - 1

print(maxDist)