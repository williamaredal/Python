from datetime import datetime, timedelta
import matplotlib.pyplot as plt

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


# function that finds out how much of your drug is in your system each day when doses are taken with a given interval (1 day to 31 day intervals)
doseOverTime = []
def RecursiveDoseInterval(dose, doseHourInterval, dosesN, halfLifeHours, bodyDosage=0, dosesTaken=0):
    if (dosesTaken < dosesN):
        previousDoseInterval = datetime.now() + timedelta(hours=(doseHourInterval * (0 if ((dosesTaken - 1) < 0) else (dosesTaken - 1)) ))
        currentDoseInterval = datetime.now() + timedelta(hours=(doseHourInterval * dosesTaken))

        halfLifeTimes = ((currentDoseInterval - previousDoseInterval).total_seconds() / 3600 / halfLifeHours)
        currentBodyDosage = (bodyDosage / (2**(halfLifeTimes) ) + dose)

        doseOverTime.append((currentDoseInterval.strftime('%d-%H:%M'), currentBodyDosage))

        RecursiveDoseInterval(dose=dose, doseHourInterval=doseHourInterval, dosesN=dosesN, halfLifeHours=halfLifeHours, bodyDosage=(currentBodyDosage), dosesTaken=(dosesTaken + 1))

    else:
        ax = plt.axes()
        # plotting requires work as the x-axis is easily filled and unreadable when dosesN gets large.
        # when this is added strftime can include month-day-hour:minute
        plt.plot([time[0] for time in doseOverTime], [dose[1] for dose in doseOverTime])
        plt.show() 
        return doseOverTime


# function calls:

RecursiveDoseInterval(200, 24, 7, 18)
#print(HowManyHalfCycles(200, 4, 0.05))
