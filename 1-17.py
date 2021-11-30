while True:
    sum = input("金額：")
    if sum == "q":
        print("終了")
        break
    try:
        sum = int(sum) * 1
    except ValueError:
        print("エラーです。もう一度入力してください。")
        continue
    while True:
        num = input("人数：")
        try:
            result = round(sum / int(num))
            print("一人当たり",result,"円です。")
            break
        except ValueError:
            print("文字が入力されました。もう一度入力してください。")
        except ZeroDivisionError:
            print("0で計算されました。もう一度入力してください。") 
