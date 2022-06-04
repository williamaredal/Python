import random
import enchant
import os

def DisplayWord(word):
    word_hidden = ""
    for w in word:
        if w == " ":
            word_hidden += " "
        
        else:
            word_hidden += "-"

    # refreshes terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to hangman.")
    print("The current word is: ", word_hidden)



def GameLoop():
    englishDictionary = enchant.Dict("en_US")
    hangmanWorld = {}
    gameOver = False

    # players enter valid words for their opponents to guess
    p1Word = input("Player 1, please enter a valid word for Player 2 to guess: ")
    while englishDictionary.check(p1Word) == False:
        p1Word = input("Player 1, please enter a valid word for Player 2 to guess: ")

    p2Word = input("Player 2, please enter a valid word for Player 1 to guess: ")
    while englishDictionary.check(p2Word) == False:
        p2Word = input("Player 2, please enter a valid word for Player 1 to guess: ")
    
    hangmanWorld["p1Word"] = p1Word
    hangmanWorld["p1Guesses"] = []
    hangmanWorld["p2Word"] = p2Word
    hangmanWorld["p2Guesses"] = []


    # game loop begins
    while gameOver == False:
        p1Letter = input("Player 1, please enter a single letter: ")
        p2Letter = input("Player 2, please enter a single letter: ")

        hangmanWorld["p1Guesses"].append(p1Letter)
        hangmanWorld["p2Guesses"].append(p2Letter)

        