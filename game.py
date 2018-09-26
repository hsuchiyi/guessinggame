import random
r = random.randint(1,100)
while True:
    R = input('請猜數字?(1~100)')
    R = int(R)
    if R == r:
        print('答對了!')
        break
    elif R > r:
        print('比這個小')
    else:
        print('比這個大')        