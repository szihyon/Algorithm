def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    #초 변환
    mi, sec = map(int, video_len.split(":"))
    video_len = mi*60 + sec
    mi, sec = map(int, pos.split(":"))
    pos = mi*60 + sec
    mi, sec = map(int, op_start.split(":"))
    op_start = mi*60 + sec
    mi, sec = map(int, op_end.split(":"))
    op_end = mi*60 + sec
    
    

    
    while commands:
        if op_start <= pos < op_end: #이동 전 오프닝 구간인 경우
            pos = op_end
        if commands[0] == "next":   #뒤로 가기
            if pos + 10 > video_len:    #비디오 끝보다 뒤인 경우
                pos = video_len #비디오 끝으로 이동
            elif op_start <= pos + 10 < op_end: #오프닝 구간인 경우
                pos = op_end    #오프닝 끝으로 이동
            else:   #그 외
                pos = pos + 10  #10초 뒤로 이동
        elif commands[0] == "prev": #앞으로 가기
            if pos - 10 < 0:    #비디오 시작보다 앞인 경우
                pos = 0 #시작 부분으로 이동
            elif op_start <= pos - 10 < op_end: #오프닝 구간인 경우
                pos = op_end
            else:
                pos = pos - 10
        if op_start <= pos < op_end: #이동 후 오프닝 구간인 경우
            pos = op_end
        del commands[0]
    
    mi = pos // 60
    sec = pos % 60
    
    answer = f"{mi:02}:{sec:02}"
            
    return answer