opposite=[5,3,4,1,2,0] 
# [0,1,2,3,4,5]의 반대편 인덱스들임
# 반대편 숫자 쌍들은 아래와 같기 때문
# lst[0], lst[5] 
# lst[1], lst[3] 
# lst[2], lst[4]

n=int(input())
lst=[]
for _ in range(n):  # 주사위의 값들 n번 입력받아 리스트에 추가하기
    lst.append(list(map(int,input().split())))

maxval=0
for i in range(1,7):
    val=0
    bottom_num=i    # 첫번째 주사위의 바닥에 올 수 있는 숫자(1~6) 모두 돌려보기
    for dice in range(n):   # 주사위 하나씩 꺼내서 계산해보기 
        nums=lst[dice][:]   # 주사위 숫자들
        bottom_index=nums.index(bottom_num) # 바닥숫자의 인덱스
        top_index=opposite[bottom_index]    # 반대편 숫자의 인덱스
        bottom_num=nums[top_index] # 이게 다음 주사위의 바닥이 됨
        nums[bottom_index]=0   # 아래와 위를 제외한 옆면 숫자들끼리 비교하기 위해 0으로 설정
        nums[top_index]=0
        val+=max(nums)  # 옆면 숫자들 중 최대값
    if val>maxval:
        maxval=val
print(maxval)