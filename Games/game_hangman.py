import random

game_playing = "yes"
game_over = False
selection = ["Awkward","Bagpipes","Banjo","Bungler","Croquet","Crypt","Dwarves","Fervid","Fishhook","Fjord","Gazebo","Gypsy","Haiku","Haphazard","Hyphen","Ivory","Jazzy","Jiffy","Jinx","Jukebox"]
current_word = selection[random.randint(0,len(selection)-1)]
guess = []

# kalle funksjon etter spillet er over for å velge nytt ord til hvert spill
def generate_word(word):
    word_hidden = ""
    for w in word:
        word_hidden += "-"

# lage dynamisk formel for antall gjettinger ut fra ordlengde og erstatte '(10-len(guess))'
        if len(word_hidden) == len(word):
            print("Welcome to hangman.")
            print("The current word is: ", word_hidden, "\nYou have 10 guesses.")
            break


def check_guess(letter, word):
    word_hidden = ""

    if len(str(letter)) >= 2 or letter in guess:
        print("Please reenter a single character.")
        return False
    if len(guess) >= 9:
        return True

    elif len(str(letter)) == 1:
        guess.append(letter)
        
        for w in word:

# lage dynamisk formel for antall gjettinger ut fra ordlengde og erstatte '(10-len(guess))'
            if w not in guess:
                word_hidden += "-"
            if w in guess:
                word_hidden += w
            if len(word_hidden) == len(word):
                print("Welcome to hangman.", "\nThe current word is: ", word_hidden, "\nYour guesses:", guess, "\nGuesses left:", 10-(len(guess)))
                break

        if word_hidden == word:
            return True
        else:
            return False

generate_word(current_word)
while game_playing == "yes" or game_playing == "y":

    if check_guess(str(input("Guess a single letter:")), current_word):
        game_playing = input("Game is over.Type (y/yes) to play again, or any other letter to exit.")

        if game_playing == "yes" or game_playing == "y":
            guess = []
            current_word = selection[random.randint(0,len(selection)-1)]
            generate_word(current_word)
        else:    
            exit()