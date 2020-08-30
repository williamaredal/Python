import random

min = 1
max = int(input("How many numbers to guess from?(higher than 1)"))
number = random.randint(min, max)

guess_again = "yes"

while guess_again == "yes" or guess_again == "y":
    guess = int(input("What is your guess?"))

    if guess != number:
        if guess > number:
            print("Your guess was too high.")
        if guess < number:
            print("You guess was too low.")

    if guess == number:
        print("Congratulations! You guessed,", guess, "which is correct.")
        guess_again = input("Press (y) to guess again, or (any key) to exit.")

        if guess_again == "yes" or guess_again == "y":
            max = int(input("How many numbers to guess from?(higher than 1)"))
            number = random.randint(min, max)
        else:
            quit()