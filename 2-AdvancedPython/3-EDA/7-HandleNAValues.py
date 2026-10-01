# It is responsibility of a data professional to handle Missing or Null values

import pandas as pd
from Tools.scripts.pathfix import preserve_timestamps

df = pd.read_csv("weather_data.csv")
print(df.columns)
print(type(df['day'][0])) # this is string
# converting to date format
df = pd.read_csv("weather_data.csv",parse_dates=['day'])
print(type(df['day'][0])) # now converted to time stamp
df.set_index('day',inplace=True)
print(df)
# replacing Na values with 0
df.fillna(0) # in case you want to modify the df use inplace = True
print(df)
# replace NA values of temp and windspeed with mean
df.fillna({
    "temperature" : df.temperature.mean(),
    "windspeed" : df.windspeed.mean(),
    "event" : "No Event"

}) # in case you want to modify the df use inplace = True

print(df)
print(df.fillna(method='ffill')) # ffill is forward fill

# backward fill
print(df.fillna(method='bfill'))

# by default the fill is wrt to rows, now you can fill wrt to columns using axis

print(df.fillna(method='bfill',axis = "columns")) # this is meaningless in this scenario

# limiting how many rows to change consecutively

print(df.fillna(method='ffill' , limit=1))

# fills NA value with the avg of upper and below value
print(df)
print(df.interpolate())
print(df.dropna())
print(df.dropna(how='all')) # if all values in row are na drop them
print(df.dropna(thresh=2)) 