import pandas as pd

df = pd.read_csv("movies.csv")
print(df.columns)

# print unique industries
print(df['industry'].unique())
print(type(df['industry'].unique()))

# print unique languages
print(df['language'].unique())

# print number of hollywood and bollywood movies
print(df['industry'].value_counts())

# print number of movies in each language
print(df['language'].value_counts())

# storing selective columns of a df to new df

df_new = df[['title','imdb_rating','industry']]
print(df_new)

# print movies between 200 and 2010

df1 = df[(df['release_year'] >= 2000) & (df['release_year'] <= 2010)]
print(df1)

# print the movies only from marvel studios
print(df['studio'].unique())
print(df[df['studio'] == 'Marvel Studios'])

print(df.describe())
print(df.info())

# print the movie with max and min imdb_rating

print(df[df['imdb_rating'] == max(df['imdb_rating'])])
print(df[df['imdb_rating'] == min(df['imdb_rating'])])

# printing just the title
print(df[df['imdb_rating'] == max(df['imdb_rating'])].title)
print(df[df['imdb_rating'] == min(df['imdb_rating'])].title)

# find the age of the movie

from datetime import datetime
print(df['release_year'].apply(lambda rel_year : datetime.now().year - rel_year ))

# here the function inside apply is applied on release_year

# find the profit for each movie and add profit column to df
# axis = 1 , function is applied to each row
# x is row here
df['profit'] = df.apply(lambda x : x['revenue'] - x['budget'], axis=1)
print(df)

# index operation
# data frames have index by default and current index is
print(df.index) # current index is from 0 to 37
# we can set any column as index

# inplace = True modifies the original database
df.set_index('title',inplace=True)

print(df.head(3))

print(df.index)

#index is something like a hashmap, where index acts like a key and we can access
#the entire row using this index
print(df.loc['Pather Panchali'])
print(df.loc[['Pather Panchali','Pushpa: The Rise - Part 1']])

print(df.iloc[0])
print(df.iloc[1:3])

df.reset_index(inplace=True)
print(df.index)

