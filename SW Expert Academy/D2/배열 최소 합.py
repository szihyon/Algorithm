T = int(input())

def abc(level, sum):    # 중복되지 않는 경로를 탐색하여 모든 합을 구해보고 최소값을 얻는 함수  
    global minSum
    if sum > minSum: return # 최소값을 넘어가면 더 이상 탐색하지 않고 종료(탐색 횟수를 줄일 수 있음)
    if level == n:  # 마지막 행까지 sum값을 더하면 종료. 행과 열이 중복되지 않게 lst[행번호][열번호]를 모두 더한 최종 값이 됨
        if sum < minSum:
            minSum = sum
        return
    for i in range(len(nums)):
        if used[i] == 0:    # 아직 사용하지 않은 열의 숫자(인덱스)면
            used[i] = 1 # 사용표시 해준 후    
            abc(level+1, sum + lst[level][nums[i]]) # 매개변수로 sum값 더해가기. 더하는 값은 행과 열이 중복되지 않은 lst[행번호][열번호]
            used[i] = 0 # 마지막 level까지 도달한 후 돌아올 때는 다시 0으로 초기화 

for tc in range(1, T+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    nums = [i for i in range(n)]    # 인덱스로 사용될 숫자 목록
    used = [0]*len(nums)    # 이미 사용한 인덱스를 다시 사용하지 않기 위해 기록
    minSum = 21e8
    abc(0, 0)   # 0번 인덱스, sum=0부터 시작
    print(f"#{tc} {minSum}")

    
    
###    
# 실패했던 코드 
T = int(input())
# 
# def abc(level): # 인덱스 순열 생성하는 함수
#     if level == n:
#         global paths
#         paths.append(path[:])
#         return
#     for i in range(len(nums)):
#         if used[i] == 0:
#             used[i] = 1
#             path[level] = nums[i]
#             abc(level+1)
#             used[i] = 0
# 
# for tc in range(1, T+1):
#     n = int(input())
#     lst = []
#     for i in range(n):
#         lst.append(list(map(int, input().split())))
#     nums = [i for i in range(n)]
#     path = [0]*n
#     paths = []
#     used = [0]*len(nums)
#     abc(0)
# 
#     minSum = 21e8
#     for p in range(len(paths)): # paths에 저장된 인덱스 순열대로 하나씩 더하기
#         sum = 0
#         for i in range(len(lst)):
#             sum += lst[i][paths[p][i]]
#         if sum < minSum:    # 모든 조합의 합들 중 가장 작은 값 저장
#             minSum = sum
# 
#     print(f"#{tc} {minSum}")
