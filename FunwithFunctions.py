def say_hello(numri):
    for numri in range(0, numri):
        print('"Hello"')

say_hello(10)


def funx2(nr1,nr2):
    print(nr1 + nr2)

funx2(1,17)

#i = int(3)
#for i in range(0, i):
#    say_hello(3)


def half(nr):
    print(nr)
    while True:
        if nr > 0:
            nr = round(nr/2)
            print(nr)
        else: 
            break 

half(50)
input("Press Enter to Exit...")
