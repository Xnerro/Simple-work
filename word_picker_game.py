import random
import os

items = []

word = open("words.txt", "r")


for text in word:
    items.append(text.strip())

z = random.choice(items)
bags = []
test = z
j = False
k = 0
l = 1

for i in range(len(z)):
    bags.append("_")
    i += 1
bags[0] = z[0]

while j != True:
    print("Guest Word")
    print(bags)
    x = input("Input Word: ")

    if x == z[l]:
        os.system("clear")
        bags[l] = x
        l += 1
        if l == len(bags):
            print("The Word is")
            print(bags)
            print("Your answer correct")
            j = True
    else:
        os.system("clear")
        print("Your answer wrong")
        k += 1
        if k == 3:
            print("You lose")
            j = True


print()
