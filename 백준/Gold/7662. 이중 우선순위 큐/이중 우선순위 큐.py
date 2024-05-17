# I : 삽입
# D 1 : 최댓값 삭제
# D -1 : 최솟값 삭제
# 최댓값, 최솟값 출력하기. Q가 비어있다면 EMPTY 출력하기

import heapq

T = int(input())
for tc in range(T):
    k = int(input())
    min_Q = []
    max_Q = []
    nums = dict() # 딕셔너리를 활용하여 값 조회

    for _ in range(k):
        O, N = input().split()
        N = int(N)
        # 데이터 삽입
        if O == 'I':
            if N not in nums:
                nums[N] = 1
            else:
                nums[N] += 1
            heapq.heappush(min_Q, N)
            heapq.heappush(max_Q, -N)
        # 데이터 삭제
        else:
            if N == 1: # 최댓값 삭제
                while max_Q:
                    max_val = -1 * heapq.heappop(max_Q)
                    if max_val in nums and nums[max_val] > 0:
                        nums[max_val] -= 1
                        if nums[max_val] == 0:
                            del nums[max_val]
                        break
                    # min_Q.remove(-val)
            else: # 최솟값 삭제
                while min_Q:
                    min_val = heapq.heappop(min_Q)
                    if min_val in nums and nums[min_val] > 0:
                        nums[min_val] -= 1
                        if nums[min_val] == 0:
                            del nums[min_val]
                        break
                    # max_Q.remove(-val)

    # if max_Q and min_Q:
    #     print(-1*heapq.heappop(max_Q), heapq.heappop(min_Q))
    # else:
    #     print('EMPTY')

    while max_Q and (-max_Q[0] not in nums or nums[-max_Q[0]] == 0):
        heapq.heappop(max_Q)
    while min_Q and (min_Q[0] not in nums or nums[min_Q[0]] == 0):
        heapq.heappop(min_Q)

    results = []
    if max_Q and min_Q:
        max_val = -max_Q[0]
        min_val = min_Q[0]
        results.append(f"{max_val} {min_val}")
    else:
        results.append("EMPTY")
    print("\n".join(results))
