import random
start = input('請決定隨機範圍初始值: ')
end = input('請決定隨機範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count = count + 1 
    R = input('請猜數字?')
    R = int(R)
    if R == r:
        print('答對了!')
        break
    elif R > r:
        print('比這個小')
    else:
        print('比這個大')
    print('這是你猜的第', count, '次')        