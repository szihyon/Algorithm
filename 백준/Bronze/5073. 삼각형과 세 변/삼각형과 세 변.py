while(True):
    a, b, c = map(int, input().split())
    lst = [a, b, c]
    if a==b==c==0:
        break

    if a==b==c:
        print("Equilateral")
    elif a>=b+c or b>=a+c or c>=a+b:  #  a + b + c - max_ <= max_
                                      #  2 * max(a, b, c) >= a + b + c
        print("Invalid")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
