import sys

print("Please choose one of the beverages: (1)Coca-Cola, (2) Sprite,(3) Pepsi,(4) Fanta,(5) Coffee")

beverages = {1: "Coca-Cola", 2: "Sprite", 3: "Pepsi", 4: "Fanta", 5: "Coffee"}

x = int(input("Input your beverage code: "))

if 1 <= x <= 5 :
    print("Here's your:", beverages.get(x))

else:
    print("Error. Choice was not valid,here is your money back.")
    sys.exit(1)
