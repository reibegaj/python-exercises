import sys


x = int
i = int(0)


while x != i - 1:
    print("Provide a number different than", (i))
    x = int(input())
    i = i + 1
else:
    print("Hey, your were not supposed to enter", (x))
