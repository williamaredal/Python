from getpass import getpass
import enchant
import os

def IntroScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to 2 player hangman.\n")
    print("Your inputs will be hidden from your opponent, but fear not! You are indeed typing.")
    print("The first player to guess the word set by your opponent wins!\n\n")


def GameScreen(p1Word, p1Guesses, p2Word, p2Guesses):
    p1HiddenWord = ""
    p2HiddenWord = ""

    for word in p1Word:
        for letter in word:
            if letter in p2Guesses:
                p1HiddenWord += letter

            else:
                p1HiddenWord += "_"

        p1HiddenWord += " "

    for word in p2Word:
        for letter in word:
            if letter in p1Guesses:
                p2HiddenWord += letter

            else:
                p2HiddenWord += "_"

        p2HiddenWord += " "

    # refreshes terminal to show new state of game
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Player 1:")
    print("Word to guess: ", p2HiddenWord)
    print("Guesses: ", (p1Guesses if len(p1Guesses) > 0 else {}), "\n")

    print("Player 2:")
    print("Word to guess: ", p1HiddenWord)
    print("Guesses: ", (p2Guesses if len(p2Guesses) > 0 else {}), "\n\n")


def VictoryScreen(playerN, players, word):
    opponents = [p for p in players]
    opponents.remove(playerN)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nPlayer ", playerN, " wins!")
    print("Dun dun DUN! Player", opponents[0], "was sent to the gallows...")
    print("The word given by player", opponents[0], "was: ", word)


def GameLoop():
    englishDictionary = enchant.Dict("en_US")
    hangmanWorld = {}
    gameOver = False

    IntroScreen()

    # players enter valid words for their opponents to guess, and initializes game variables
    p1Word = getpass(prompt="Player 1, please enter a valid word for Player 2 to guess: ")
    while englishDictionary.check(p1Word) == False:
        p1Word = getpass(prompt="Player 1, please enter a valid word for Player 2 to guess: ")

    p2Word = getpass(prompt="Player 2, please enter a valid word for Player 1 to guess: ")
    while englishDictionary.check(p2Word) == False:
        p2Word = getpass(prompt="Player 2, please enter a valid word for Player 1 to guess: ")
    
    hangmanWorld["players"] = [1, 2]
    hangmanWorld["p1Word"] = p1Word
    hangmanWorld["p1Chars"] = set(p1Word)
    hangmanWorld["p1Guesses"] = set()
    hangmanWorld["p2Word"] = p2Word
    hangmanWorld["p2Chars"] = set(p2Word)
    hangmanWorld["p2Guesses"] = set()

    # game loop begins
    while gameOver == False:
        GameScreen(hangmanWorld["p1Word"], hangmanWorld["p1Guesses"], hangmanWorld["p2Word"], hangmanWorld["p2Guesses"])

        # players enter valid chars as their guesses
        p1Letter = getpass(prompt="Player 1, please enter a single letter: ")
        while len(p1Letter) != 1 or p1Letter.isalpha() == False or p1Letter in hangmanWorld["p1Guesses"]:
            p1Letter = getpass(prompt="Player 1, please enter a single letter: ")

        p2Letter = getpass(prompt="Player 2, please enter a single letter: ")
        while len(p2Letter) != 1 or p2Letter.isalpha() == False or p2Letter in hangmanWorld["p2Guesses"]:
            p2Letter = getpass(prompt="Player 2, please enter a single letter: ")

        # players enter valid words as their guesses
        hangmanWorld["p1Guesses"].add(p1Letter)
        hangmanWorld["p2Guesses"].add(p2Letter)

        # checks if the word set by p1 has been guessed p2 and vice versa 
        p1Victory = hangmanWorld["p1Guesses"].issuperset(hangmanWorld["p2Chars"])
        p2Victory = hangmanWorld["p2Guesses"].issuperset(hangmanWorld["p1Chars"])
        if p1Victory and p2Victory:
            print("The game is a draw. Nobody is hanged today...")
            gameOver = True

        elif p1Victory:
            VictoryScreen(1, hangmanWorld["players"], hangmanWorld["p2Word"])
            gameOver = True
        
        elif p2Victory:
            VictoryScreen(2, hangmanWorld["players"], hangmanWorld["p1Word"])
            gameOver = True
        
        else:
            GameScreen(hangmanWorld["p1Word"], hangmanWorld["p1Guesses"],  hangmanWorld["p2Word"], hangmanWorld["p2Guesses"])        



if __name__ == "__main__":
    GameLoop()