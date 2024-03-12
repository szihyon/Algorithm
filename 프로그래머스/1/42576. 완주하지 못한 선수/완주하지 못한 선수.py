def solution(participant, completion):
    answer = ''
    n = len(participant)
    n2 = len(completion)
    dic = dict()
    for i in range(n):
        if participant[i] not in dic:
            dic[participant[i]] = 1
        else:
            dic[participant[i]] += 1
    for i in range(n2):
        dic[completion[i]] -= 1
    for key, value in dic.items():
        if value == 1:
            answer = key
    
    return answer