num = input("何個購入しますか？：")
try:
    price = 120 / int(num)
    print("一個当たり", price ,"円です。")
except:
    print("エラー")
finally:
    print("終了")
