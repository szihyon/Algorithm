def solution(n, m, section):
    answer = 0
    end = 0
    for start in section:
        if start > end: 
            end = start + m - 1 
            answer += 1
    return answer