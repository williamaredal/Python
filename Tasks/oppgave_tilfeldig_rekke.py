import random

# oppdatere til input verdi 'int(input("Hvor mange skal delta i "))'
deltagere = 6
min = 1

rekke = []
par_rekke = []

for i in range(min, deltagere+1):
    print(i)
    rekke.append(i)

random.shuffle(rekke)
print(rekke, "par_rekke", len(rekke))

while len(rekke) > len(par_rekke):

    for number in rekke:
        tilfeldig = random.randint(min, deltagere)
        verdi = number

        while tilfeldig:
            if tilfeldig != verdi and tilfeldig not in par_rekke:
                par_rekke.append(tilfeldig)
                break
            else:
                tilfeldig = random.randint(min, deltagere)
                continue

        print(par_rekke, "par_rekke", len(par_rekke))