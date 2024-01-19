def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    n = len(score) // m
    for i in range(1, n+1):
        minV = score[i*m-1]
        answer += minV * m
    return answer