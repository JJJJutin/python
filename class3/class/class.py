
"""我是Python,今年31歲了"""
# name = 'Python'
# age = 31
# new_str = "我是" + name + "," + "今年" + str(age) + "歲了"
# new_str_1 = "我是%s,今年%d歲了" % (name, age)
# new_str_2 = "我是{},今年{}歲了".format(name, age)
# new_str_3 = "我是{a},今年{b}歲了".format(b=age, a=name)
# new_str_4 = f"我是{name},今年{age}歲了"

"""錯誤偵測"""
# try:
#     num = int(input('請輸入一個數字'))
#     total = num + 1
#     print(total)
# except ValueError:
#     print('請輸入數字')
# except:
#     print('發生錯誤')
# else:
#     print('成功執行')
# finally:
#     print('程式結束')

"""錯誤偵測-BMI計算"""
# try:
#     h = float(input('請輸入身高(公分):'))
#     w = float(input('請輸入體重(公尺):'))
# except:
#     print('發生錯誤')
# else:
#     print("好的")
#     bmi = w / (h/100)**2
#     print('你的BMI為', bmi)
# finally:
#     print("程式結束")

"""布林值"""
# print(1 == 1)
# # True
# print(1 != 0)
# # True
# print(1 >= 2)
# # False
# print(1 <= 2)
# # True
# print(1 > 2)
# # False
# print(1 < 2)
# # True