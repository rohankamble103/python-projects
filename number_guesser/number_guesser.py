import random

top_of_range = input("Type any number you want: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter the number larger that 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()
guesses = 0
random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Guess the number:- ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a digit next time:- ")
        continue

    if user_guess == random_number:
        print("You got it in ", guesses, "guesses")
        break
    else:
        if user_guess > random_number:
            print("You are above the number")
        else:
            print("You are below the number")
