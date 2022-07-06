x = int(input("Input your score: "))
print("Your score is:", x )

if x ==100:
    print ("You got a perfect score")

elif 90 <= x <= 99:
    print ("You got an A")

elif 70 <= x <= 79:
    print ("You got a B")

elif 70 <= x <= 79:
    print ("You got a C")

elif 60 <= x <= 69:
    print ("You got a D")

elif 0 <= x <= 59:
    print ("You got a F")

else: print("Please provide a valid score (between 0-100)")
