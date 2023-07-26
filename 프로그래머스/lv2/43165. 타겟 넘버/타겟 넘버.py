def solution(numbers, target):
    # numbers.insert(0, 0)
    n = len(numbers)
    answer = 0
    answer = dfs(0, 0, n, numbers, target, answer)
    return answer

def dfs(sumV, level, n, numbers, target, answer):
    if level == n:
        if sumV == target:
            answer += 1
        return answer

    answer = dfs(sumV+numbers[level], level+1, n, numbers, target, answer)
    answer = dfs(sumV-numbers[level], level+1, n, numbers, target, answer)

    return answer
    
    