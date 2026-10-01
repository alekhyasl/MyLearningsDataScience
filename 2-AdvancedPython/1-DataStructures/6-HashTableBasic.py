stock_prices = []
with open("StockPrices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = int(tokens[1].strip())
        stock_prices.append([day,price])
print(stock_prices)

# find price on mar=09
# here to find price on specific day using list, the complexity is order of n

for element in stock_prices:
    if element[0] == 'Mar-09':
        print("stock price on Mar-09 is ",element[1])

# by using dictionary to find price on specific day , the complexity is order of 1

stock_prices = {}
with open("StockPrices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = int(tokens[1].strip())
        stock_prices[day]= price
print(stock_prices)
print(stock_prices['Mar-09'])

print("------------------------")

'''
In python hash table/hash map is implemented using dictionary
complexity of acessing value in dictionary is O(1) 
complexity of inserting/deleting value in dictionary is O(1) 
for accessing the value in dictionary, hash function is applied on the key
to find out the index where the value is stored
There are different ways of implementing hash function
one way is as below
suppose we have m   a   r   c  h        6
Ascci value     109 97  114 99 104  32  54   sum = 609
since the size of my array is 10
perform modulus of 609 with 10 which is 9
so here hash function generates an index of 9 , where the value is stored

'''

# implementing of hash function in python

def get_hash(key):
    h=0
    for char in key:
        h += ord(char) # ord function finds ASCII value of character
    return h%100  # assuming 100 as size of list

print(get_hash('MAR-09'))

