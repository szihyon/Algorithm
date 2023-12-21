def solution(a, b, c, d):
    answer = 0
    str_lst = [a, b, c, d]
    str_count = []
    for s in str_lst:
        str_count.append(str_lst.count(s))
    
    # 같은 숫자가 4개일 때
    if str_count.count(4) == 4:
        answer = 1111 * str_lst[0]
    # 같은 숫자가 3개일 때
    elif str_count.count(3) == 3:
        for i in range(len(str_count)):
            if str_count[i] != 3:
                answer = (10 * str_lst[str_count.index(3)] + str_lst[i])**2
                break
    # 같은 숫자가 2개씩 있을 때
    elif str_count.count(2) == 4:
        p = str_lst[0]
        for i in range(1, len(str_lst)):
            if str_lst[i] != p:
                q = str_lst[i]
        answer = (p+q)*abs(p-q)
    # 모두 다른 숫자일 때
    elif str_count.count(1) == 4:
        answer = min(str_lst)
    # 같은 숫자 2개, 서로 다른 숫자 1개씩 있을 때
    else:
        diff_n = [] # 중복 없는 숫자 리스트
        for i in range(len(str_count)):
            if str_count[i] == 1:
                diff_n.append(str_lst[i])
        answer = diff_n[0] * diff_n[1]
    return answer