
from doctest import testfile


testList = [0, 1, 2, 3, 4, 5]

for el in testList:
    print(el)

print()

for el in range(len(testList)):
    print(el)

print()

for el in range(0, len(testList)):
    print(el)

print()


# Bit language experimentation

char1 = "0"
char2 = "1"
char3 = "2"

bitSize = 2
bitExponent = 3

bitSequenceOne = ""
for n in range(bitSize ** bitExponent):

    if 2 ** n > bitSize ** bitExponent:
        bitSequenceOne += char1
    elif 2 ** n == bitSize ** bitExponent:
        bitSequenceOne += char2
    elif 2 ** n < bitSize ** bitExponent:
        bitSequenceOne += char3

print(bitSequenceOne)