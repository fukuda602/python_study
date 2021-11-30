a = int(input("取り出す位置："))
b = ["blue","red","green","yellow"]
leng = len(b)
if -leng <= a < leng:
    c = b[a]
    print(c)
else:
    print("Error") 
