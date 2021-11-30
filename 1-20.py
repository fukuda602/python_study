t = 1
menu = ["にんじん","かぼちゃ","なす","レタス","じゃがいも"]
print(menu,end="")
try:
    ques = int(input("嫌いな食べ物はありますか？："))
except ValueError:
    print("Error")
    t = 0 
while t == 1:
    try:
        menu.pop(ques)
        print(menu)
        ans = input("まだ変更しますか？：")
        if ans == 'q':
            print("メニューは",menu,"です。")
            break
        else:
            ans = int(ans) * 1
        ques = int(ans)
    except:
        print("Error")
        break
        
        
         
