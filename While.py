import sys


x = int(input("Provide a number different than 5: "))
i = int(1)

while i < 10 and x != 5:
    x = int(input("Provide a number different than 5: "))
    i = i + 1
else:
    print("Wow, you're more patient then I am, you win.")
