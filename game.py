import random
r = random.randint(1,100)
count = 0
while True:
    count = count + 1 
    R = input('請猜數字?(1~100)')
    R = int(R)
    if R == r:
        print('答對了!')
        break
    elif R > r:
        print('比這個小')
    else:
        print('比這個大')
    print('這是你猜的第', count, '次')        