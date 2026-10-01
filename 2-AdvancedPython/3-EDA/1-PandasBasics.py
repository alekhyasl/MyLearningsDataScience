# without using pandas framework
import csv

# print movie ratings for all movies, bollywood movies and hollywood movies

def calculate_ratings(data,industry = None):
    rating = []
    for row in data:
        if row[3] != 'NULL' and  (row[1] == industry or industry is None) :
            rating.append(float(row[3]))

    max_rating = max(rating)
    min_rating = min(rating)
    avg_rating = sum(rating)/len(rating)
    return max_rating,min_rating,avg_rating

with open("movies.csv") as f:
    data = list(csv.reader(f))
    print(data)
    header = data[0]
    data = data[1:]

max_rating,min_rating,avg_rating = calculate_ratings(data)
print(f"Ratings of all movies, min rating : {min_rating} , max_rating : {max_rating} , avg_rating : {avg_rating}")

max_rating,min_rating,avg_rating = calculate_ratings(data,"Bollywood")
print(f"Ratings of Bollywood movies, min rating : {min_rating} , max_rating : {max_rating} , avg_rating : {avg_rating}")

max_rating,min_rating,avg_rating = calculate_ratings(data,"Hollywood")
print(f"Ratings of Hollywood movies, min rating : {min_rating} , max_rating : {max_rating} , avg_rating : {avg_rating}")

# using pandas framework
import pandas as pd

df = pd.read_csv("movies.csv")
# df is a data frame object
# data frame stores the data in tabular format
# print(df)
print(df.head())# prints first 5 rows by default
print(df.tail())# prints last 5 rows by default
print(df.head(6))
print(df.sample(4)) # prints randomly 4 rows
print(df[2:7])
print(df.shape)

# print avg imdb rating
print(df.imdb_rating)  # we can print like df['imdb_rating']
print(type(df.imdb_rating)) # this is of type Series
print(dir(df.imdb_rating))
print("min rating is : ",df.imdb_rating.min())
print("max rating is : ",df.imdb_rating.max())
print("average rating is : ",df.imdb_rating.mean())

df_b = df[df['industry'] == 'Bollywood']
print("min rating of bollywood movies is : ",df_b['imdb_rating'].min())
print("max rating of bollywood movies is : ",df_b['imdb_rating'].max())
print("average rating of bollywood movies is : ",df_b['imdb_rating'].mean())


df_h = df[df['industry'] == 'Hollywood']
print("min rating of Hollywood movies is : ",df_h['imdb_rating'].min())
print("max rating of Hollywood movies is : ",df_h['imdb_rating'].max())
print("average rating of Hollywood movies is : ",df_h['imdb_rating'].mean())
