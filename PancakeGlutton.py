from operator import itemgetter
from collections import OrderedDict

i = 1
pancakes = {
    "Person 1": int(),
    "Person 2": int(),
    "Person 3": int(),
    "Person 4": int(),
    "Person 5": int(),
    "Person 6": int(),
    "Person 7": int(),
    "Person 8": int(),
    "Person 9": int(),
    "Person 10": int()
}

for x in pancakes.keys():
    print("Provide the number of pancakes eaten by Person",i)
    pancakes[x] = input()
    i = i + 1
    #print(pancakes)

print("The person who ate the most pancakes is:",max(pancakes, key=pancakes.get))

print("The person who ate the least pancakes is:",min(pancakes, key=pancakes.get))



#OrderedDict = (sorted(pancakes.items(), key=itemgetter(1)))

dict_sorted =sorted(pancakes.items(), key=lambda x: x[1])

print(type(dict_sorted))
