N, B = input().split()
B = int(B)
answer = 0

for idx, num in enumerate(N[::-1]):
    if num.isalpha():
        answer += (ord(num)-55)*(B**idx)
    else:
        answer += int(num)*(B**idx)

print(answer)