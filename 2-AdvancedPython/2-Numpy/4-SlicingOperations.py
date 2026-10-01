import numpy as np

a1 = np.array([1,2,3,4,5,6,7,8])

print(a1[0:2]) # print from 0 to 1 , index 2 is not included

print(a1[2:])  # print from index 2 till end

print(a1[-1])

print(a1[-1:0]) # prints empty as moving from -1 to 0 is in -ve direction
# where as increment of 1 is in +ve direction, so both are contradicting

print(a1[-1:0:-1])

print(a1[-3:])

b = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# print 6 from b array

print(b[1,2])

# print 7 from array b

print(b[2,0])

print(b[-1])

print(b[-1,0:2])

print(b[:,1:3])

# hstack , vstack

# Customer ID, Name
c = np.array([
    [101, 'Mira'],
    [102, 'Abdul'],
    [103, 'Andrea']
])
# Customer Id, Purchase Amount, Purchase Date
d = np.array([
    [101, 250.50, '2023-08-01'],
    [102, 150.00, '2023-08-02'],
    [103, 300.75, '2023-08-01']
])

print(np.hstack((c,d))) # merges horizontally

e = np.array([
    [104, 'Venkat'],
    [105, 'John'],
    [106, 'Kathy'],
])

print(e)

print(np.vstack((c,e)))

# splitting the data using hsplit,vsplit

transactions = np.array([
    [101, 'Mohan', 250.50, '2023-08-01'],
    [102, 'Bob', 150.00, '2023-08-02'],
    [103, 'Fatima', 300.75, '2023-08-01'],
    [104, 'David', 400.20, '2023-08-03'],
    [105, 'Aryan', 330.1, '2023-08-04'],
])

print(np.hsplit(transactions,[3]))

a,b = np.hsplit(transactions,[3])

print(a)
print(b)

c,d = np.vsplit(transactions,[3])
print(c)
print(d)

monthly_sales = np.array([30,33,35,28,42])
sales_target = 32
result = monthly_sales < sales_target
print(result)

print(monthly_sales[result]) # sales when they are low than target

# max sales
print(np.max(monthly_sales))

# at which month the sales are max
index = np.argmax(monthly_sales)
print(index)

# sales at peak month
print(monthly_sales[index])

transactions = np.array([
    [101, 'Mohan', 250.50, '2023-08-01'],
    [102, 'Bob', 150.00, '2023-08-02'],
    [103, 'Fatima', 300.75, '2023-08-01'],
    [104, 'David', 400.20, '2023-08-03'],
    [105, 'Aryan', 330.1, '2023-08-04'],
])

# in transactions get the max transaction amount

transaction_amounts = transactions[:,2]
transaction_amounts = transaction_amounts.astype(float)
print(transaction_amounts)

print(np.max(transaction_amounts)) # prints max transaction amount

index = np.argmax(transaction_amounts) # gets the index of max transaction amount

print(transactions[index]) # prints record of max transaction amount

# get a record with transaction id 102

transaction_id = transactions[:,0]
print(transactions[transaction_id == '102'])