import pandas as pd

df = pd.read_csv("weather_by_cities.csv")
print(df.columns)

# get max temp in each city in dataset
print(df['city'].unique())
print(df[df['city'] == 'new york']['temperature'].max())

# if we use the above way , it is difficult to do when we have large data sets
# which has large number of cities
# so in this case we can use group by

g = df.groupby('city')

# g is the data frame group by object
# group by creates individual dataframe for each city , where key is the city name
# for each data frame

for city,data in g:
    print("city : ",city)
    print(data)
    # print max temp in each city
    print("max temp : " ,data.temperature.max())

print(g.get_group('paris'))

print(g.max()) # get the max values of each column for each group which is here city

print(g.min())

print(g.describe())

print(g.size()) # gives size of sub data frames

# group by temp of different ranges

def grouper(df,idx,column):
    if 80 <= df[column].loc[idx] <=90:
        return "80-90"
    elif 50 <= df[column].loc[idx] <= 60:
        return "50-60"
    else:
        return 'others'


g = df.groupby(lambda idx : grouper(df,idx,'temperature'))

for key,data in g:
    print("key : ",key)
    print("Data : ",data)