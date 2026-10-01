import pandas as pd

df = pd.read_csv("stock_data.csv",skiprows=1)
print(df) # skiprows skip the first row here

df = pd.read_csv("stock_data.csv",header=1)
print(df) # first row is considered as header
print(df.columns)

# to customise column names
df = pd.read_csv("stock_data.csv",header=1,names=["stock_symbol",'eps', 'revenue', 'price', 'people'])
print(df)

# to read only n number of rows
df = pd.read_csv("stock_data.csv",header=1,nrows=3)
print(df)

# NA values
df = pd.read_csv("stock_data.csv",header=1, na_values = {
    'eps' : ['not available'],
    'revenue' :[-1],
    'price' : ['n.a.']
    })
print(df)

df = pd.read_csv("stock_data.csv", header = 1, na_values = ['not available',-1,'n.a.'])
print(df)

# adding pe to csv file

df['pe'] = df['price']/df['eps']
print(df)

# writing to csv
df.to_csv("pe1.csv",index=False,header=False)