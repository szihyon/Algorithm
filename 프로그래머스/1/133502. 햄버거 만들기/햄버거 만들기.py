def solution(ingredient):
    answer = 0
    lst = []
    for i in range(len(ingredient)):
        lst.append(ingredient[i])
        if lst[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                lst.pop()
    return answer