# 每回合顯示功能選單：
# 1. 新增餐點：印出菜單，請使用者輸入餐點編號，可以重複輸入一樣的餐點
# 2. 移除餐點：移除使用者輸入名稱的所有餐點
# 3. 提交菜單：顯示每樣餐點的名稱及數量後關閉系統
a=[]
k = []
j = []
while True:
    print(a)
    print("1.新增餐點")
    print("2.移除餐點")
    print("3.提交菜單")
    try:
        turnin = int(input("請輸入功能選項:"))
    except:
        print("分不清數字和文字喔")
    if turnin == 3 :
        for i in a:
            if not(i in k):
                k.append(i)
        for i in k:
            print(f"{i}:{a.count(i)}")
        print("已提交菜單")
        break
    elif turnin == 2 :
        print(a)
        x = input("請輸入想移除的餐點完整名稱:")
        while x in a:
            a.remove(x)
        print("移除成功")
    elif turnin == 1 :
        print("1.蘋果汁")
        print("2.柳橙汁")
        print("3.葡萄汁")
        drinkint= input("請輸入想新增的飲料編號:")
        if drinkint == "3" :
            print("您點的飲料是葡萄汁")
            a.append("葡萄汁")
        elif drinkint == "2" :
            print("您點的飲料是柳橙汁")
            a.append("柳橙汁")
        elif drinkint == "1" :
            print("您點的飲料是蘋果汁")
            a.append("蘋果汁")
        else:
            continue
    else:
        print("看不懂數字嗎?沒上過幼稚園嗎?")
    
