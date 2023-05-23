import random

number = random.randint(1, 32)

print("I thought of a number. Can you guess it?")
while 1:
    guess = int(input ("Your guess: "))
    if guess > number:
        print("The number is less than your guess.")
    elif guess < number:
        print("The number is greater than your guess")
    else:
        print("You just found the number!")
        break

print("Thank you for playing with me.")