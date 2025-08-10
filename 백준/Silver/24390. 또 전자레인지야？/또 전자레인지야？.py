minutes, seconds = input().split(":")
minutes = int(minutes)
seconds = int(seconds)
button = 1

if seconds >= 30:
    seconds -= 30
if seconds < 30:
    button += seconds//10 
    seconds = 0

if minutes >= 10:
    button += minutes//10
    minutes -= (minutes//10) * 10
if minutes >= 1:
    button += minutes//1
    minutes -= (minutes//1) * 1

print(button)   
