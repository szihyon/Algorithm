n, l = map(int, input().split())
traffic_light = []
red_and_green = []
for i in range(n):
    d, r, g = map(int, input().split())
    traffic_light.append(d)
    red_and_green.append((r,g))
traffic_light = [0] + traffic_light + [l]

time = 0
for i in range(n+1):
    if i == n:
        time += traffic_light[i+1] - traffic_light[i]
        break
    time += traffic_light[i + 1] - traffic_light[i]
    check = time % sum(red_and_green[i])
    if check < red_and_green[i][0]:
        time += red_and_green[i][0] - check

print(time)