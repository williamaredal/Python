from datetime import datetime, date
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

# Find out how many days there are until the date you're waiting for
print('Welcome to How long until...')
untilDate = (parse(input('What date are you waiting for?')))

while (untilDate == '') or (isinstance(untilDate, datetime) == False):
    # Loops until valid date is given
    untilDate = parse(input('Please enter a valid date. (month with day as number)')).date

currentDate = datetime.now()

# If the date is in the next year this is corrected for
if currentDate.month > untilDate.month:
    untilDate = untilDate + relativedelta(years=1)

dayDifference = untilDate - currentDate

print('There are ' + str(dayDifference.days) + ' days until that date.')
