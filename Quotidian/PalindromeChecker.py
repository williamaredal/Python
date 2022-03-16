from datetime import datetime
import sys

def CheckIfPalindrome(word):
    return word == word[::-1]

def CheckYearsPalindrome(startYear, endYear=datetime.today().year):
    if (startYear >= 0) and (endYear > startYear):
        count = len([y for y in range(startYear - 1, endYear + 1) if CheckIfPalindrome(str(y))])
    else:
        print('Enter valid years to check for palindromes between')
    return count

def main():
    inputYear = int(sys.argv[1])
    CheckYearsPalindrome(inputYear)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()