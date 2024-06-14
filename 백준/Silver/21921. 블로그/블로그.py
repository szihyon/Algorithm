N, X = map(int, input().split())
visitors = list(map(int, input().split()))
start = 0
end = start+X-1     # -1주의
sumV = sum(visitors[start:end+1])   # +1주의
maxV = 0
cnt = dict()

while end < N:
    # 최대값 갱신
    if sumV > maxV:
        maxV = sumV

    # 각 구간의 합 딕셔너리에 저장
    if sumV not in cnt:
        cnt[sumV] = 1
    else:
        cnt[sumV] += 1

    if end == N-1:  # end가 N-1인 조건까지 딕셔너리 반영 후 반복문 종료
        break

    # 현재 start 빼고
    sumV -= visitors[start]
    start += 1
    # 다음 end 더하고
    end += 1
    sumV += visitors[end]

if maxV:
    print(maxV)
    print(cnt[maxV])
else:
    print("SAD")

