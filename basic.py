n = input()
if int(n) >= 100:
    result = "合格"
else:
    n = int(n) - 100
    result = "不合格／" + str(n)
print(result)

    

