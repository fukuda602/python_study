numlist = [3, 4.2, 10, "x", 1, 9]
sum = 0

for num in numlist:
    if not isinstance(num, (int ,float)):
        print("文字が出力されました。")
        continue
    sum += num
    print(num, "/" ,sum)
