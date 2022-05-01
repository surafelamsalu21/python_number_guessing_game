import random

from numpy import NaN
top_of_range = input("Type a number\n")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number graterthan '0'")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess\n")
    user_guess = int(user_guess)
#     if user_guess.isdigit():
    if True:  # we should check this out why it is not working ?
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess < random_number:
        print("colder")
    elif user_guess > random_number:
        print("Hotter")
    else:
        if user_guess == random_number:
            print(f"You got it and it took you {guesses} trial")
            quit()
        else:
            print("Got it wrong")
