def solution(answers):
    answer = []
    n = len(answers)
    
    p1 = []
    p1_num = [1, 2, 3, 4, 5]
    for i in range(n):
        p1.append(p1_num[i%5])
    
    p2 = []
    p2_num = [1, 3, 4, 5]
    for i in range(n):
        if i % 2 == 0:
            p2.append(2)
        else:
            p2.append(p2_num[((i-1)//2)%4])
    
    p3 = []
    p3_num = [3, 1, 2, 4, 5]
    for i in range(n):
        p3.append(p3_num[(i//2)%5])
    
    p1_cnt = 0
    p2_cnt = 0
    p3_cnt = 0
    for i in range(n):
        if answers[i] == p1[i]:
            p1_cnt += 1
        if answers[i] == p2[i]:
            p2_cnt += 1
        if answers[i] == p3[i]:
            p3_cnt += 1

    win = max(p1_cnt, p2_cnt, p3_cnt)
    if p1_cnt == win:
        answer.append(1)
    if p2_cnt == win:
        answer.append(2)
    if p3_cnt == win:
        answer.append(3)
    
    return answer