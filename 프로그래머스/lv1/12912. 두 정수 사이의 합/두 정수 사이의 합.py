def solution(a, b):
    answer = 0
    sumV = 0
    if a < b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a
    l = num2-num1+1
    for i in range(num1, num2+1):
        sumV += i
    answer = sumV
    return answer