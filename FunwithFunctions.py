def say_hello(numri):
    for numri in range(0, numri):
        print('"Hello"')

say_hello(8)


def funx2(nr1,nr2):
    print(nr1 + nr2)

def half(nr):
    print(nr)
    while True:
        if nr > 0:
            nr = round(nr/2)
            print(nr)
        else:
            break

half(10)
input("Press Enter to Exit...")
