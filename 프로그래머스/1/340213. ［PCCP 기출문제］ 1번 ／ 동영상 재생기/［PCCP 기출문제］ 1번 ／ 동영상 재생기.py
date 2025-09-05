def solution(video_len, pos, op_start, op_end, commands):
    """
    - 오프닝 구간에 있으면 자동으로 오프닝 끝으로 이동
    - next: 10초 앞으로, prev: 10초 뒤로
    """
    
    def time_to_seconds(time_str):
        """mm:ss 형식을 초로 변환"""
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds
    
    def seconds_to_time(seconds):
        """초를 mm:ss 형식으로 변환"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"
    
    def skip_opening(position, op_start, op_end):
        """오프닝 구간에 있으면 오프닝 끝으로 이동"""
        return op_end if op_start <= position < op_end else position
    
    # 시간을 초로 변환
    video_len_sec = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)
    
    # 시작 위치가 오프닝 구간이면 오프닝 끝으로 이동
    current_pos = skip_opening(current_pos, op_start_sec, op_end_sec)
    
    # 명령어 처리
    for command in commands:
        if command == "next":
            # 10초 앞으로 이동
            new_pos = current_pos + 10
            
            # 동영상 끝을 넘으면 동영상 끝으로
            if new_pos >= video_len_sec:
                current_pos = video_len_sec
            else:
                current_pos = new_pos
                
        elif command == "prev":
            # 10초 뒤로 이동
            new_pos = current_pos - 10
            
            # 동영상 시작보다 앞이면 시작으로
            if new_pos < 0:
                current_pos = 0
            else:
                current_pos = new_pos
        
        # 명령어 처리 후 오프닝 구간 체크
        current_pos = skip_opening(current_pos, op_start_sec, op_end_sec)
    
    return seconds_to_time(current_pos)