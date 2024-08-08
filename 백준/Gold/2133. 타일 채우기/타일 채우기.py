n = int(input())

dp = [0]*(n+1)
dp[0] = 1
if n >= 2: dp[2] = 3 # N이 2일 때 3가지

# 짝수인 경우
for i in range(4, n+1, 2): # 4부터 시작
    dp[i] = 4*dp[i-2] - dp[i-4]

print(dp[n])