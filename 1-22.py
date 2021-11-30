i = [4,32,536,7,5,1]
print("デフォ",i)
a = i.copy()
a.sort()
print("昇順",a)
b = i.copy()
b.sort(reverse = True)
print("降順",b)
c = i
print("代入",c)
c[0] = 100
print("変更",c)
print("cデフォ",i)
d = sorted(i)
print("昇順2",d)
print("確認",i)
