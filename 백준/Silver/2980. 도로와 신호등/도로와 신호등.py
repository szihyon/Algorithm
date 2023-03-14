# 설계는 각 신호등에서 7초일 땐 어떤색 불일지, 13초일 땐 어떤색 불일지 아무 숫자나 대입해보면서 생각하며 규칙을 찾아 이루어졌습니다. 
# check = 시간 % (빨간불 지속시간 + 초록불 지속시간) 이라고 할 때,
# 만약 check가 빨간불 지속시간보다 작다면, (빨간불 대기시간 - check)만큼 기다려야 합니다(시간++).
# 그 외에는 각 신호등 사이의 간격만큼 시간이 더해집니다. 
# 출발지부터 첫번째 신호등까지, 그리고 마지막 신호등부터 도착지까지의 거리도 계산해야 하기 때문에, 신호등 위치를 담은 리스트 양 옆에 [0]과 [l]을 추가하여 계산했습니다.

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
