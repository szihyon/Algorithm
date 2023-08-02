def solution(prices):
    n = len(prices)
    answer = [0]*n
    for i in range(n-1):
        flag = 0
        cnt = 0
        for j in range(i+1, n):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                answer[i] = cnt + 1
                flag = 1
                break
        if flag == 0:
            answer[i] = cnt
    answer[n-1] = 0
    return answer