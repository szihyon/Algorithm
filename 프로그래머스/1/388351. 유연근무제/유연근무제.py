def solution(schedules, timelogs, startday):
    answer = 0
    
    #시간을 분으로 변환
    for i in range(len(schedules)):
        h = schedules[i] // 100
        m = schedules[i] % 100
        schedules[i] = h*60 + m + 10 # +10분  
    for i in range(len(timelogs)):
        for j in range(len(timelogs[i])):
            h = timelogs[i][j] // 100
            m = timelogs[i][j] % 100
            timelogs[i][j] = h*60 + m 
    
    cnt_lst = []
    for i in range(len(timelogs)):
        day = startday
        cnt = 0
        for j in range(len(timelogs[i])):
            if timelogs[i][j] <= schedules[i]:  #출근 인정 시각보다 일찍 오면
                cnt += 1    #카운트
            else:   #출근 인정 시각보다 늦었지만 주말이면
                if day == 6 or day == 7:
                    cnt += 1
            day += 1    #다음 요일
            if day == 8:
                day = 1
        cnt_lst.append(cnt)
    
    answer = cnt_lst.count(7)   #7일 출근 인정 받으면 상품 수령
    
    return answer