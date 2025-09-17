def solution(diffs, times, limit):
    n = len(diffs)
    
    # 특정 숙련도 level로 모든 퍼즐을 풀 때 걸리는 총 시간 계산
    def calculate_time(level):
        total_time = 0
        for i in range(n):
            if diffs[i] <= level:
                # 숙련도가 충분한 경우: 현재 퍼즐 시간만 소요
                total_time += times[i]
            else:
                # 숙련도가 부족한 경우: 틀린 횟수만큼 추가 시간 소요
                mistakes = diffs[i] - level
                # (현재 퍼즐 + 이전 퍼즐) × 틀린 횟수 + 현재 퍼즐
                if i > 0:
                    total_time += (times[i] + times[i-1]) * mistakes + times[i]
                else:
                    # 첫 번째 퍼즐의 경우 이전 퍼즐이 없음
                    total_time += times[i] * mistakes + times[i]
        return total_time
    
    # 이진탐색으로 최소 숙련도 찾기
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if calculate_time(mid) <= limit:
            answer = mid  # 가능한 숙련도 저장
            right = mid - 1  # 더 낮은 숙련도로도 가능한지 탐색
        else:
            left = mid + 1  # 숙련도를 높여야 함
    
    return answer