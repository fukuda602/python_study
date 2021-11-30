import random
num = list(range(1,101))
result = []
for i in range(50):
    root = random.choice(num)
    result.append(root)
    num.remove(root)
while True:
    try:
        ques = int(input("受験番号："))
        if ques in result:
            print("合格")
            exit()
        else:
            print("不合格")
            exit()
    except ValueError:
        print("Error")
