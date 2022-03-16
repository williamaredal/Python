import json
from statistics import mode
import sys
import os

def OrganizeEmailAccounts():
    '''
    Helps you organize the internet accounts you have created with your email account(s) to a json file 
    '''
    cwd = os.getcwd()
    filename = "//" + sys.argv[1]
    
    existingFile = False
    # checks if file exists
    if os.path.exists(cwd + filename):
        existingFile = True


    with open(cwd + filename, mode='r+') as file:
        classificationList = {}
        
        # opens json file and fills classificationList with existing entries        
        if existingFile and len([row for row in file]) > 0:
            print("Currently does not support json loading")
            
        emailInput = input("Please enter an email to link to website accounts:\n")
        classificationList[emailInput] = {} 
        userInput = ""

        while userInput.lower() != "exit":

            # add limit to number of elements printed in interface

            # The user interface presented in console
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Current accounts in list by email:")

            for email in classificationList.keys():
                print(email + ":")
                for website in classificationList[email]:
                    print("   " + website)

            userInput = input("Write a website where '" + emailInput + "' was used to create an account, 'exit' to quit this program or 'finished' to write list to json:\n")
            
            # verifies user inputs
            if userInput.lower() == "exit":
                sys.exit()
            if userInput.lower() == "finished":
                break
            
            classificationInput = input("Please classify this account. (Type 'k' for 'keep', 'd' for 'delete'):\n")
            while classificationInput == "" or classificationInput.lower() not in ["k", "keep", "d", "delete"]:
                classificationInput = input("Please enter a valid classification. (Type 'k' for 'keep', 'd' for 'delete'):\n")

            # ads the valid inputs to the list
            classificationList[emailInput][userInput] = classificationInput

        # when finished script continues here
        file.write(json.dumps(classificationList))


def main():
    OrganizeEmailAccounts()

if __name__ == "__main__":
    #main()

    # version that only accepts existing file
    if len(sys.argv) > 1 and sys.argv[1].endswith(".json"):
       main()
    
