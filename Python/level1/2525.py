hour, minute = map(int, input().split())
durationTime = int(input())

if (hour >=0 or hour <= 23) and (minute >= 0 or minute <= 59):
    minute = minute + durationTime
    
    while minute > 59:
        minute = minute - 60
        hour = hour + 1
        
        if hour > 23:
            hour = 0
        
        if minute <= 59:
            break

print(hour, end=' ')
print(minute)
