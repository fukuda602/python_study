while True:
    num = input("何個購入されますか？：")
    if num == 'q':
        print("終了します。")
        break
    try:
        price = 120 * int(num)
        print(price,"円です。")
    except:
        print("エラーです。もう一度入力してください。")

