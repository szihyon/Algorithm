def solution(k, score):
    answer = []
    lst = []
    for s in score:
        if len(answer) < k:
            lst.append(s)
        else:
            min_index = lst.index(min(lst))
            if s > min(lst):
                lst[min_index] = s
        answer.append(min(lst))
                
    return answer