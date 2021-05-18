from datetime import datetime, timedelta

# NB! I do not have medical experience with drug half-life so take this calculator with a grain of salt

# function that finds out how many half life cycles the drug has to pass before the initial dosage has lost its effect (with low and high estimate)
def HowManyHalfCycles(dose, halfLifeTimeHours, requirement):
    halfTimeDelta = timedelta(hours=halfLifeTimeHours)
    todayReference = datetime.now()
    eliminated = False
    cycles = 0

    while eliminated == False:
        cycles += 1
        todayReference += halfTimeDelta
        currentDose = (dose / (2**cycles))

        if ((currentDose / dose) <= requirement): # if initial dose reaches 5% or 1% of original ammount it's effect can it be assumed to have dissapeared?
            eliminated = True
        else:
            continue
    
    return('With a half-life of ' + str(halfLifeTimeHours) + ' hours, it took ' + str(cycles) + ' cycles before reaching <5% of the original dose of ' + str(dose) + '. Meaning you would no longer feel affected at ' + str(todayReference))


print(HowManyHalfCycles(200, 4, 0.05))
