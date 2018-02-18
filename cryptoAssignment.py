import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import time

def minute_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df

time_delta = 1
df = minute_price_historical('BTC', 'USD', 9999, time_delta)

x_axis = df.timestamp
y_axis = df.close

# Initialize a Figure
fig = plt.figure()

# Add Axes to the Figure
#fig.add_axes([0,0,1,1])

# Set up Axes
ax = fig.add_subplot(111)

# Plotting the data
ax.plot(x_axis, y_axis)

#Plotting to our canvas
#plt.plot(x_axis, y_axis)
plt.xticks(rotation=45)
#Showing what we plotted
plt.show()