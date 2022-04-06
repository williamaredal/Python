import os
import re

cwd = os.getcwd()
wordEnding = "wordEnding.txt"
wordToMatch = "wordToMatch.txt"

lettersToReplace = "e".lower()
replacementLetters = "ks".lower()

wordEndingDict = {}
replacedLetterDict = {}

with open(cwd + "//" + wordEnding) as f:
    words = [word.replace('\n', '').lower() for word in f]
    for word in words:
        if word.endswith(lettersToReplace.lower()):
            wordReplaced = word.lower().replace(lettersToReplace, replacementLetters)
            wordEndingDict[wordReplaced] = word.lower()


with open(cwd + "//" + wordToMatch) as f:
    words = [word.replace('\n', '').lower() for word in f]
    for word in words:
        if word.lower().count(lettersToReplace) > 0:
            wordReplaced = word.lower().replace(lettersToReplace, replacementLetters)
            replacedLetterDict[wordReplaced] = word


print(wordEndingDict)
print()
print(replacedLetterDict)
print()


for newWord in wordEndingDict:
    try:
        replacedLetterDict[newWord]
        print("Match", newWord, " : ", replacedLetterDict[newWord])
    
    except KeyError:
        continue

