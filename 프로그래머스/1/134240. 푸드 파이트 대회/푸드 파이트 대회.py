def solution(food):
    answer = ''
    n = len(food)
    for i in range(1, n):
        answer += str(i)*(food[i]//2)
    temp = answer[::-1]
    answer += '0'
    answer += temp
    return answer