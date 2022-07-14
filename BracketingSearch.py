from random import seed
from random import randint

rnd = randint(0, 100)

i = 0

print(rnd)

while rnd:
    value = int(input("Take a guess and I'll say higher or lower: "))
    i = i + 1    
    if value > rnd:
        print("too high")

    elif value < rnd:
        print("too low")
    elif value == rnd:
        print("Wow, you guessed it right!")
        print("It took you",i,"times to guess it right" )
        break
