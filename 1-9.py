from random import randint
num = []

while len(num) < 10 :
    a = randint(-10,90)
    if a < 0 :
        print("マイナスが実行されたため中止します。")
        break
    if a in num :
        continue
    num.append(a)
else:
    print(num)
