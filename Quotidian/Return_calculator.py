import matplotlib.pyplot as plt

run = 'y'

while run.strip() == 'y':
    initialReturn = float(input('The initial return on investment (0 if none): '))
    annualReturn = float(input('Annual return on investment: '))
    investmentTimetable = int(input('Number of whole years to graph returns over: '))

    modifyValue = input('Would you like to change your inputs? (y/n) ').lower()

    while modifyValue.strip() == 'y':
        initialReturn = float(input('The initial return on investment (if none write 0): '))
        annualReturn = float(input('Annual return on investment: '))
        investmentTimetable = int(input('Number of whole years to graph returns over: '))

        modifyValue = input('Would you like to modify your inputs again? (y/n)').lower()


    returnOverTime = [float((initialReturn / investmentTimetable) + annualReturn) for n in range(1, investmentTimetable + 1)]
    returnByYear = [float( (initialReturn / n) + annualReturn) for n in range(1, investmentTimetable + 1)]


    fig1, ax = plt.subplots()
    fig1.canvas.set_window_title('Graphing of return of investment over time')
    b1 = ax.plot([year for year in range(1, investmentTimetable + 1)], returnOverTime, label='Average return over years')
    b2 = ax.plot([year for year in range(1, investmentTimetable + 1)], returnByYear, label='Investment return by year')

    plt.show()

    run = input('Would you like to calculate return of something else? (y/n) ').lower()