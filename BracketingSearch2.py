from random import seed
from random import randint

rnd = randint(0, 100)

i = 0

while rnd:
    print(rnd)
    value = input("Tell me if my guess is ""too high"" or ""too low"", or tell ""right"" if I got it right: ")
    i = i + 1    
    if value == "too low":
        rnd += 1

    elif value == "too high":
        rnd -= 1


    elif value == "right":
        print("Wow, I guessed it right!")
        print("It took me",i,"times to guess it right" )
        break

