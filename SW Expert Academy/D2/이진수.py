# 방법 1
T = int(input())

for tc in range(1, T + 1):
    n, number = input().split()

    ans = ''
    for x in number:
        num = int(x, 16)
        for j in range(3, -1, -1):
            bit = 1 if num & (1 << j) else 0
            ans += str(bit)
    print(f"#{tc} {ans}")
    
    
    
# 방법 2
# def convert16to2(x):
#     num = int(x, 16)
#     rt = ""
#     for _ in range(4):
#         if num % 2 == 1:
#             rt = "1" + rt
#         else:
#             rt = "0" + rt
#         num = num // 2
#     return rt
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     n, number = input().split()
#
#     print(f"#{tc}", end=' ')
#     for x in number:
#         num = convert16to2(x)
#         print(num, end="")
#     print("")



# 방법3
# 딕셔너리로 만들기
