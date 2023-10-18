hour, minute = map(int, input().split())
cost = int(input())

if minute + cost > 59:
    add_hour = (minute + cost) // 60
    add_minute = minute + cost
    hour = hour + add_hour
    minute = add_minute % 60
    if hour > 23:
        hour = hour - 24
    print(hour, minute)
else:
    print(hour, minute + cost)