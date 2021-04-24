from datetime import datetime

def CheckIfPalindrome(word):
    return word == word[::-1]

def CheckYearsPalindrome(startYear, endYear=datetime.today().year):
    if (startYear >= 0) and (endYear > startYear):
        count = len([y for y in range(startYear - 1, endYear + 1) if CheckIfPalindrome(str(y))])
    else:
        print('Enter valid years to check for palindromes between')
    return count

print(CheckYearsPalindrome(int(input('Start year')) ))