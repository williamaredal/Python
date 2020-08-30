import pandas as pd
import datetime
import pandas_datareader
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()
ticker = 'AAPL'

# currently does not work because of:
#   pandas_datareader.exceptions.ImmediateDeprecationError: 
#   Google finance has been immediately deprecated due to large breaks in the API without the
#   introduction of a stable replacement. Pull Requests to re-enable these data
#   connectors are welcome.

df = pandas_datareader.data.DataReader(ticker, 'google', start, end)


print(df)

df['Adj Close'].plot()

plt.show()
