import sys
input = sys.stdin.readline

N = int(input())
n = N // 4

for i in range(n):
    print("long", end=" ")
print("int")


# 본 문제에 대한 답변: 숫자가 너무 크면 숫자 타입에 담기지 못해서, 문자열로 받아서 한 자리씩 직접 더해야 한다. 
