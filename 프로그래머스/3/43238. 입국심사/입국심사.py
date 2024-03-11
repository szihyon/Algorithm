def solution(n, times):
    min_time = 1
    max_time = max(times) * (n-1) # 모든 사람이 가장 오래 걸리는 심사대를 이용할 때의 시간

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        total = sum(mid_time // time for time in times)

        if total >= n: # 모든 사람을 심사할 수 있는 경우, 시간을 줄여본다
            max_time = mid_time - 1
        else: # 모든 사람을 심사할 수 없는 경우, 시간을 늘린다
            min_time = mid_time + 1
            
    answer = min_time
    return answer