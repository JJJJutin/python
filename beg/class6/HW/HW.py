
# put = int(input('請輸入:'))
# x = put
# y = 0
# z = 0
# for z in range(x):
#     x = x - 1
#     z = z * 2 + 1
#     print(" " * x + "*" * z)
# for z in range(put):
#     print(" " * (put - 1) + "*")
put = int(input('請輸入:'))
for z in range(put):
    print(" " * (put-1-z) + "*" * (z * 2 + 1))
for z in range(put):
    print(" " * (put - 1) + "*")