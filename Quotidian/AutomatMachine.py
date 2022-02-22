
# D = ( 1^n | n % 2 = 0 | n > 1, n < 11)
testString = ""
rule1 = {
    "character" : "1",
    "modulus" : 2,
    "set" : (1, 11)
}

def Node(nodeInput, rule):
    validStrings = []
    outputString = nodeInput
    automatCharacter = str(rule["character"])
    automatStringRule = rule["modulus"]

    # start and end of interval
    setStart = rule["set"][0]
    setEnd = rule["set"][1]

    for _i in range(setStart, setEnd):
        # finds out if the input is the initial state
        if outputString == "":

            # if the node should append a 1
            if outputString.count(automatCharacter) % automatStringRule == 0:
                validStrings.append(outputString)

        else:

            if outputString.count(automatCharacter) % automatStringRule == 0:
                validStrings.append(outputString)
            


        outputString = outputString + str(rule["character"])


    return validStrings


print(Node(testString, rule1))