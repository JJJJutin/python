# l = ['a', 'b', 'c']
# l
# l[0] = 'A'
# l

# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)

# l = [1, 2, 3]
# l.append(4)
# print(l)

# l = [9, 1, -4, 3, 7, 11, 3]
# print(l.count(3))

# l = ['a', 'b', 'c', 'a']
# l.remove('a')
# print(l)

# l = [1, 2, 3]
# l.insert(0, 'A')
# print(l)

# l = [1, 2, 3]
# l.pop()  刪除最後一個編號
# print(l)

# l = [1, 2, 3]
# l.pop(0)  刪除編號零
# print(l)

# l = [3, 1, 5, 4, 2]
# l.sort()
# print(l) ans = [1, 2, 3, 4, 5]

# l = [3, 1, 5, 4, 2]
# l.sort(reverse=True)
# print(l) ans = [5, 4, 3, 2, 1]

# l = [3, 1, 5, 4, 2]
# l.reverse()
# print(l) ans = [2, 4, 5, 1, 3] 鏡像

# l = ['a', 'b', 'c', 'a']
# index = l.index('a') 找位子 (從左到右第一個)
# print(index) 

# L = [2, 1, 4, 5, 1, 1, 6, 1, 1]
# print(not (1 in L))
# while 1 in L:
#     L.remove(1)

# print(L)

a=[]
while True:
    x= input("輸入e就離開程式，請輸入想新增的資料:")
    if x == "e":
        break
    a.append(x)
    print(a)
while True:
    x= input("del(e=exit):")
    if x == "e":
        print("881")
        break
    else:
        print(not (x in a))
        while x in a:
            a.remove(x)
k = []
for i in a:
    if not(i in k):
        k.append(i)
for i in k:
    print(f"{i}有{a.count(i)}個")

