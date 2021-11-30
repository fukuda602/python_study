from random import randint
ture = 0 
miss = 0

while miss < 3:
    a = randint(0, 100)
    b = randint(0, 100)
    ques = f"{a} + {b} = "
    ans = input(ques)
    if ans == 'q':
        break          
    if int(ans) == a + b:
        ture += 1
        print("正解")
    else:
        miss += 1
        print("不正解" + "×" * miss)
        
print("-" * 20)
print("正解数:" + str(ture) + " 不正解数:" + str(miss))
