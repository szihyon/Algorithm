def solution(players, m, k):
    answer = 0
    time = [0]*24
    n = len(players)
    for i in range(n):
        if players[i] >= m: #m명 이상이면
            added = players[i]//m - time[i] #최소 player//m 필요
            if added >= 1:  #증설하는 경우
                answer += added
                for j in range(k): #운영 시간 기록
                    if i+j < 24:
                        time[i+j] += added

    return answer