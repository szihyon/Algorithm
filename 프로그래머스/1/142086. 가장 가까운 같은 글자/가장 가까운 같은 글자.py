def solution(s):
    answer = []
    lst = [] 
    for i in range(len(s)):
        if s[i] not in lst:
            answer.append(-1)
            lst.append(s[i])
        else:
            reversed_lst = lst[::-1]
            find_index = len(lst) - reversed_lst.index(s[i]) - 1
            answer.append(i - find_index)
            lst.append(s[i])
    return answer