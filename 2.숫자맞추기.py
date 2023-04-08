import random

x = random.randint(1,20)
i = 0
while i < 4 :
    a = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요 : ".format(4-i)))
    if x==a:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(i+1))
        i=5
    elif x>a:
        print("UP")
        i += 1
    else :
        print("Down")
        i += 1
