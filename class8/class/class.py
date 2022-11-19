# ['蘋果', '香蕉', '葡萄']

# []
# ['蘋果']
# ['a', 'b']
# [1, 2, 3]

# [1, 2] + ['b', 'c']

# [1, 2] * 2

# l = ['a', 'b', 'c']
# l[0]
# l[1]
# l[2]

# l = [0, 1, 2, 3, 4]
# l[0:3]
# l[3:5]

# len([])
# len(['蘋果'])
# len(['a', 'b'])
# len([1, 2, 3])

# l = ['a', 'b', 'c']
# for index in range(len(l)):
#     print(l[index])

# l = ['a', 'b', 'c']
# for element in l:
#     print(element)

# max([])
# max(['蘋果', '香蕉', '橘子']) ( 沒意義 )
# max(['a', 'b']) (沒意義)
# max([1, 2, 3])

# min([])
# min(['蘋果', '香蕉', '橘子']) (沒意義)
# min(['a', 'b']) (沒意義)
# min([1, 2, 3])

# list('abc')
# list([4, 5, 6])
# list(range(3)) ans:0,1,2
# '1,2,3'.split(',') ans:['1', '2', '3']
# '2020/1/1'.split('/') ans:['2020', '1', '1']

# img = ['1', '2', '3']
# '-'.join(img) ans:['1_2_3']

# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l) ans:[1, 'b', 'c'] ['a', 'b', 'c']

juices = ["汁", "橙汁", "葡萄汁", "系統關閉"]
while True:
    for i in range(len(juices)):
        print(f'{i+1}.{juices[i]}')
    # print("1.蘋果汁")
    # print("2.柳橙汁")
    # print("3.葡萄汁")
    # print("4.系統關閉")  
    try:
      x = int(input("請輸入編號:"))
    except:
        print("分不清數字和文字喔")
    if x == len(juices) :
        print("系統已關閉")
        break
    elif x > len(juices) or x <= 0:
        print("看不懂數字嗎?沒上過幼稚園嗎?")
    else:
        print(f"您點的飲料是{juices[x-1]}")
