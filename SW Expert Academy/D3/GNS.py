import sys
sys.stdin = open("input.txt", "r")

num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for tc in range(1, T+1):
    tc, n = input().split()
    n = int(n)
    nums = input().split()
    num_lst2 = [0] * 10     # num_lst길이와 같은 빈 리스트 생성. 인덱스 순서대로 숫자크기를 의미
    for i in range(n):
        for j in range(len(num_lst)):
            if nums[i] == num_lst[j]:       # 입력받은 값을 num_lst에서 찾아서 해당 인덱스와 동일하게 num_lst에 카운트
                num_lst2[j] += 1
    print(tc)
    for i in range(len(num_lst2)):
        if num_lst2[i] > 0:     # 카운트된 횟수만큼 출력하기
            for j in range(num_lst2[i]):
                print(num_lst[i], end=" ")
    print()




