# pip install openpyxl
# use the pip command in git bash before executing below code
import pandas as pd

df_movies = pd.read_excel("movies_db.xlsx","movies")
print(df_movies.head(4))

# printing sheet names in excel file
df = pd.ExcelFile("movies_db.xlsx")
print(df.sheet_names)

df_financial = pd.read_excel("movies_db.xlsx","financials")
print(df_financial.head(5))

def standardize_currency(cur):
    if cur == "$$" or cur == "Dollars":
        return "USD"
    return cur

# converting values in a specific column
df_financial = pd.read_excel("movies_db.xlsx","financials",converters={'currency': standardize_currency })
print(df_financial.head(6))

# merging to data frames and importing data to excel

df_merged = pd.merge(df_movies,df_financial,on = 'movie_id')
print(df_merged.head(5))

df_merged.to_excel("merged_movies.xlsx","merged data",index = False)

# creating data frames

stock_df = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

print(stock_df)

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

print(df_weather)

with pd.ExcelWriter("stocks_weather.xlsx") as writer:
    stock_df.to_excel(writer,sheet_name="stocks",index=False)
    df_weather.to_excel(writer,sheet_name="weather",index=False)