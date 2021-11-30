from random import randint
a = randint(0,100)
b = randint(0,100)

if(a >= 40 and b >= 40 and a + b >= 120):
    result = "合格"
else:
    result = "不合格"

print("a:"+ str(a) + " b:" + str(b) + " 合計:" + str(a + b) + " 結果:" + result)
