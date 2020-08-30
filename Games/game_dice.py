import random
import time
min = 1
max = 6
dice_number = int(input("How many dice do you want to roll?"))

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    time.sleep(1.5)
    print("The values are....")
    for die in range(dice_number):
        print (random.randint(min, max))
    roll_again = input("Press (y) to roll the dices again, or (any key) to exit.")

while roll_again != "yes" or roll_again != "y":
    exit()