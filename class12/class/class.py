# print("here you go %d" % 94)
# print("there is%3d" % 94)
# print("your number in squidgame is %03d" % 94)

# print("here you go {0:d}" .format(94))
# print("there is {0:3d}" .format(94))
# print("your number in squidgame is {0:03d}" .format(94))

# print("here you go %f" %94)
# print("there is %.2f" %94)

# print("there is {0:f}" .format(87, 94))
# print("your number in squidgame is {1:.2f}" .format(87, 94))

# print("your number in squidgame is %s" %'Gua94')
# print("your number in squidgame is {0:s}" .format('94Gua'))
"""
a = int(input("enter a number:"))

print("this is a number %d" % a)
print("this is a number %5d" % a)
print("this is a number %05d" % a)
"""
"""
a = float(input("enter a number:"))

print("this is a number %f" % a)
print("this is a number %.2f" % a)
print("this is a number %.2f" % a)
"""
# a = int(input("enter a number for [ ]+ B:"))
# b = int(input("enter a number for A + [ ]:"))
# ans = eval("a+b")
# print(f"the answer is {ans}")

import datetime as d

# print (f"The date today is {d.date.today()}")
"""
Date = d. date.today()
print(Date.year)
print(Date.month)
print(Date.day)
"""
# Date = d. date.today()
# print(Date.strftime("%d %b %B %Y %y %A %a"))

day = input("what is your birthday?")
print(day)
birth = d.datetime.strptime(day, "%m/%d/%Y")
print(birth.date())