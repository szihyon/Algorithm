# 최대공약수를 구하는 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 메인 함수
def main():
    t = int(input()) # 테스트 케이스의 수 입력
    for _ in range(t):
        # 각 테스트 케이스에 대한 숫자 리스트 입력 (첫 번째 값은 리스트의 길이)
        nums = list(map(int, input().split()))
        answer = 0

        # 가능한 모든 쌍의 최대공약수(GCD)를 구하여 합산
        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                answer += gcd(nums[i], nums[j])

        print(answer)

if __name__ == "__main__":
    main()