def solution(s):
    answer = 0
    i = 0
    
    while i < len(s):
        x = s[i]  # 첫 글자
        x_count = 0
        other_count = 0
        
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            
            i += 1
            
            # 두 카운트가 같아지면 문자열 분리
            if x_count == other_count:
                break
        
        answer += 1
    
    return answer