import heapq
def solution(operations):
    answer = []
    min_Q = []
    max_Q = []
    nums = dict()
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        # 숫자 삽입
        if op == 'I':
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1
            heapq.heappush(min_Q, num)
            heapq.heappush(max_Q, -num)
        # 숫자 삭제
        else: 
            if num == 1: # 최댓값 삭제
                while max_Q:
                    maxV = -1 * heapq.heappop(max_Q)
                    if maxV in nums and nums[maxV] > 0:
                        nums[maxV] -= 1
                        if nums[maxV] == 0:
                            del nums[maxV]
                        break
                
            else: # 최솟값 삭제
                while min_Q:
                    minV = heapq.heappop(min_Q)
                    if minV in nums and nums[minV] > 0:
                        nums[minV] -= 1
                        if nums[minV] == 0:
                            del nums[minV]
                        break

    while max_Q and (-max_Q[0] not in nums):
        heapq.heappop(max_Q)
    while min_Q and (min_Q[0] not in nums):
        heapq.heappop(min_Q)
    
    if max_Q and min_Q:
        answer = [-max_Q[0], min_Q[0]]
    else:
        answer = [0, 0]
        
    return answer