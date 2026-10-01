# Data Structures are building blocks of Software programming
# as a software engineer we have to use right data structure for right problem
# in order to solve the problem in efficient way

# suppose you have apple stock price for 5 days
# here we can use list to store 5 days price and access it based on index

stock_price = [101,103,99,111,119]
print(stock_price[0]) # stock price at day 1
print(stock_price[1]) # stock price at day 2

# suppose you have apple stock price from march 4 to march 7
# then the best way to store is in form of key value pair by using dictionary

stock_prices = {
    'march 4' : 101,
'march 5' : 111,
'march 6' : 109,
'march 7' : 107,
}
print(stock_prices['march 6'])
print(stock_prices['march 4'])

# so here choosing the right data structure is important for efficient
# way of handing program

# for list where we store elements in contiguous memory locations
# for dictionary there is hash map function behind scene,
# on the key hash map funtion is applied and it gives the address
# where the value is stored

# so for dictionary the time complexity of search is of order O(1)
# for list the time complexity is the order of O(n)


