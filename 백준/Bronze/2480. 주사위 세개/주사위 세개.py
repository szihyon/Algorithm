import sys
input = sys.stdin.readline

nums = list((input().split()))
num1, num2, num3 = map(int, nums)

if num1 == num2 == num3:
    print(10000 + num1 * 1000)
elif num1 == num2 and num1 != num3:
    print(1000 + num1 * 100)
elif num2 == num3 and num1 != num2:
    print(1000 + num2 * 100)
elif num1 == num3 and num1 != num2:
    print(1000 + num1 * 100)
else:
    nums.sort(reverse=True)
    print(int(nums[0]) * 100)