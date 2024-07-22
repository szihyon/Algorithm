N, K = map(int, input().split())
houses = []
answer = 200000 # 최대값으로 초기화

# 집 좌표값 입력
for _ in range(N):
    x, y = map(int, input().split())
    houses.append([x, y])

# 가까운 대피소 중 가장 먼 거리 구하기
def min_distance(shelters):
    min_distances = [200000]*N  # 각 집에서 가까운 대피소까지의 거리 초기화
    # 각 집에서 대피소까지 거리 구하기
    for s in range(K):  # 각 대피소
        for h in range(N): # 각 집
            x_distance = abs(shelters[s][0] - houses[h][0])
            y_distance = abs(shelters[s][1] - houses[h][1])
            total_distance = x_distance + y_distance
            if total_distance < min_distances[h]:
                min_distances[h] = total_distance
    return max(min_distances)

# K개의 대피소 선정 (조합)
def shelter_choice(level, shelters_idx):
    global answer
    if level == K:  # K개의 대피소를 선정한 경우
        shelters = []
        for j in range(K):
            shelters.append([houses[shelters_idx[j]][0], houses[shelters_idx[j]][1]])  # 각 대피소 x,y좌표 추가하기
        max_distance = min_distance(shelters)  # 가까운 대피소 중 가장 먼 거리
        if max_distance < answer:  # 가까운 대피소 중 가장 먼 거리가 더 작으면 답 갱신
            answer = max_distance
        return
    for i in range(N):
        if level > 0 and shelters_idx[-1] < i: continue # 이미 선택된 집의 인덱스보다 큰 경우에만 진행
        shelter_choice(level+1, shelters_idx + [i]) # 다음 대피소 선택

shelter_choice(0, []) # 함수 실행
print(answer)