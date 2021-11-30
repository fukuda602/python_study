from random import randint
n = randint(0, 100)
if n >= 80:
    result = "Aクラス"
elif n >= 60:
    result = "Bクラス"
elif n >= 30:
    result = "Cクラス"
else:
    result = "不適合"
print("得点："+ str(n) + "結果："+ str(result))
