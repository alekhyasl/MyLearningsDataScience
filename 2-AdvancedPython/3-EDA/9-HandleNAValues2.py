# sometimes we have NA Values filled as 99999

import pandas as pd

df = pd.read_csv('weather_data1.csv')
print(df)

import numpy as np

print(df.replace([-99999,-88888],np.nan))

print(df.replace({
    'temperature' : -99999,
    'windspeed' : [-99999,-88888],
    'event' : 'no event'

},np.nan))

print(df.replace({
    -99999 : np.nan,
    -88888 : np.nan,
    'no event' : 'sunny'
}))

df = pd.DataFrame({
    'score': ['exceptional', 'average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})

print(df)

print(df.replace(['exceptional','good','average','poor'],[4,3,2,1]))

