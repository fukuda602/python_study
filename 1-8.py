from random import randint
num = []

while len(num) < 10 :
    a = randint(0,100)
    if a in num :
        continue
    num.append(a)

print(num)

