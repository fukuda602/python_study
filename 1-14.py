numlist = [3, 4.2, 10, 1, 9]
sum = 0

for num in numlist:
    if not isinstance(num, (int, float)):
        print("文字が出力されたため中止します。")
        break
    sum += num
else:
    print("合計：",sum)
