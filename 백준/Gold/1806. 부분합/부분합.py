N, target = map(int, input().split())
nums = list(map(int, input().split()))
start = 0
end = 0
sumV = nums[0]
ans_lst = []

while True:
    if sumV < target:
        end += 1
        if end == N:
            break
        sumV += nums[end]
    else:
        ans_lst.append(end-start+1)
        sumV -= nums[start]
        start += 1

if ans_lst:
    ans_lst.sort()
    print(ans_lst[0])
else:
    print(0)