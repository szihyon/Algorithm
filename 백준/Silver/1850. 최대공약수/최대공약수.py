A, B = map(int, input().split())
# A > B
# A와 B의 최대공약수는
# B와 A % B의 최대공약수와 동일
if A < B:
    A, B = B, A

while B != 0:
    A, B = B, A % B

print(A*'1')