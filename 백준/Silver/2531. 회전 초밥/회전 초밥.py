N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

# 초기 설정
sushi += sushi[:k-1]  # 원형 배열을 처리하기 위해 앞 부분을 뒤에 추가
unique_sushi = [0] * (d+1)
unique_sushi[c] += 1  # 쿠폰 초밥은 미리 추가
current_count = 1  # 쿠폰 초밥 하나로 시작

# 첫 k개 구간 처리
for i in range(k):
    if unique_sushi[sushi[i]] == 0:
        current_count += 1
    unique_sushi[sushi[i]] += 1

max_count = current_count

# 슬라이딩 윈도우
for i in range(k, N+k-1):
    unique_sushi[sushi[i-k]] -= 1
    if unique_sushi[sushi[i-k]] == 0:
        current_count -= 1
    
    if unique_sushi[sushi[i]] == 0:
        current_count += 1
    unique_sushi[sushi[i]] += 1

    max_count = max(max_count, current_count)

print(max_count)
