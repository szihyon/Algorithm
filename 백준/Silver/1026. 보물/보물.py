n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 두 수를 곱한 값의 최소값을 구하려면, 
# 한쪽은 큰 순서대로, 한쪽은 작은 순서대로 나열해서 곱해주면 된다.
a = sorted(a, reverse=True)
b = sorted(b)

ans = 0
for i in range(n):
    ans += a[i] * b[i]

print(ans)