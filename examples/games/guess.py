#
# Please help me to create a game which thoughts of a number
# and asks me to guess what is it.
#
import random

number = random.randint(0, 32)

while 1:
    guess = int(input("What's the number? "))
    if number > guess:
        print("The number is greater than guess.")
    elif number < guess:
        print("The number is smaller than guess.")
    else:
        print("You found the number!")
        break

print("Thank you for playing with me!")