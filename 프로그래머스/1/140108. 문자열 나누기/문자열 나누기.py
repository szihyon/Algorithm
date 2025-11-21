def solution(s):
    answer = 0
    s_lst = list(s)
    n = len(s_lst)
    now = 0
    cnt = 1
    r_cnt = 0
    for i in range(1, n):
        if now >= i:  
            continue
        if s[now] == s[i]:
            cnt += 1
        else:
            r_cnt += 1
        if cnt == r_cnt:
            answer += 1
            now = i+1
            cnt = 1
            r_cnt = 0
    if now < n:
        answer += 1
    return answer