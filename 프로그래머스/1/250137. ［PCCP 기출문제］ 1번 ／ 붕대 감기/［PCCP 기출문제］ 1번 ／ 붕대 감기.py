def solution(bandage, health, attacks):
    answer = 0
    t = bandage[0]  #시전시간
    x = bandage[1]  #초당회복량
    y = bandage[2]  #추가회복량
    
    current_health = health
    prev_attack = 0
    for attack in attacks:
        #공격 직전까지 회복
        recover_time = attack[0] - prev_attack - 1   
        current_health += recover_time * x  
        #연속 붕대감기 성공하면 체력 보너스
        if recover_time >= t:
            current_health += (recover_time//t) * y
        #최대 체력 이상으로는 회복 불가능
        if current_health > health:
            current_health = health
        #공격 받기
        current_health -= attack[1]
        if current_health <= 0:
            break
        #직전 공격 시간 갱신
        prev_attack = attack[0]
    
    if current_health <= 0:
        answer = -1
    else:
        answer = current_health
                
    
    return answer