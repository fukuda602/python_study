fruits = ["apple","orange","banana","peach"]
print(fruits,end="")
dessert = int(input("デザートはどれにしますか？："))
try:
    c = fruits.pop(dessert)
    print("デザートは",c,"です。")
except:
    print("Error")
