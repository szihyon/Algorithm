def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] % 2 == 1:
            food[i] -= 1
    n = len(food)
    for i in range(1, n):
        answer += str(i)*(food[i]//2)
    temp = answer[::-1]
    answer += '0'
    answer += temp
    return answer