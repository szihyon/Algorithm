n = int(input())

if n % 2 != 0:
    print(0)
else:
    n = n // 2
    dp = [0] * (n + 1)
    dp[0] = 1  # 초기값

    # DP 테이블 채우기
    for i in range(1, n + 1):
        dp[i] += 3 * dp[i - 1]
        for j in range(2, i + 1):
            dp[i] += 2 * dp[i - j]

    print(dp[n])