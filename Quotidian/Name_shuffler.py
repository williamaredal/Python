# Hashmap containing shuffle methods and the first numbers in these series
optionsHashmap = {
    0 : [0, 1, 'Fibonacci'],
    1 : [1, 1, 'second series'],
    2 : [1, 2, 'trird series'],
    3 : [2, 2, 'fourth series']
    }


def shuffleName(Name, Method, Direction):
    # Checks if input values are valid
    while (any(c.isdigit() for c in Name)) or (Name == '') or (Name.isspace()):
        Name = input('Enter a valid name (without numbers): ')

    while (Method.isdigit() == False ) or (int(Method) < 0) or (int(Method) > list(optionsHashmap.keys())[-1]):
        Method = input('Enter a valid option number: ')

    shuffleNumber1 = optionsHashmap[int(Method)][0] or 0
    shuffleNumber2 = optionsHashmap[int(Method)][1] or 1
    shuffledName = ''

    if Direction.lower() not in ['f', 'forward', 'b', 'backward']:
        Direction = 'forward'
    # Loops over the chars in the name and the shuffle method in parallel
    for c in name:
        aN = shuffleNumber1 + shuffleNumber2
    
        # Then the char is shuffled forward or backward by the number in the shuffle method
        if Direction.lower() in ['b', 'backward']:
            shuffledName += chr(ord(c) - aN)

        if Direction.lower() in ['f', 'forward']:
            shuffledName += chr(ord(c) + aN)
        
        shuffleNumber1 = shuffleNumber2
        shuffleNumber2 = aN


    # Returns the shuffled name
    return shuffledName



# Initial repeat value for first iteration
again = 'yes'

while again.lower() in ['y', 'yes']:
    # Prints list of shuffle options keys and name of the shuffle method from optionHashmap
    print([(key, optionsHashmap[key][2]) for key in optionsHashmap.keys()])

    # Takes inputs
    methodChoice = input('Which of the shuffle options above would you like to try? (number): ')
    direction = input('What direction would you like to shuffle? [f or forward, b or backward]: ')
    name = input('What name would you like to shuffle?: ')

    # Calls the shuffleName function
    print('Your shuffled namek: ',shuffleName(name, methodChoice, direction))

    # Repeats the super fun while loop until the user looses interest 
    again = input('Would you like to shuffle another name? [y/yes or any other key(s) to exit]: ')