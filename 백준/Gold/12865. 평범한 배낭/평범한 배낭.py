N, K = map(int, input().split()) # 물품의 수 N과 최대 무게 K
weight = [0]
value = [0]
for i in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

dp = [[0] * (K+1) for _ in range(N+1)] # 물건 i까지 고려했을 때, 무게 w를 넘지 않는 조건에서의 최대 가치 합

for i in range(1, N+1):
    for w in range(1, K+1):
        if weight[i] <= w: # 현재 물건을 배낭에 넣을 수 있는 경우
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
        else:  # 현재 물건을 배낭에 넣을 수 없는 경우
            dp[i][w] = dp[i-1][w]

print(dp[N][K])
