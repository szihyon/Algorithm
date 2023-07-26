def solution(n):
    answer = 0
    for i in range(1, n+1):
        sumV = 0
        now = i
        while sumV < n:
            sumV += now
            now += 1
        if sumV == n:
            answer += 1
    return answer