N = int(input())

room = 1

now = 1
while True:
    if N <= room:
        print(now)
        break
    else:
        room += now*6
        now += 1