# Arrays
# suppose you have apple stock price for 5 days
# here we can use array to store 5 days price and access it based on index

# stock_price = [101,103,99,111,119]
# stock_price[0] # stock price at day 1
# stock_price[1] # stock price at day 2
# RAM(random access memory) is used to store all the variables and data
# numbers are stored in binary format in memory
# integer value is stored in the form of 4 bytes in memory
# each byte is stored in one memory index

# say if stock_price[0] is stored at memory location 0x00500
# then stock_price[2] is stored at memory location 0x00500 + (2 * sizeof(integer))
# which is 0x00500 + (2*4) = 0x00508

# for the scenario 1 : what is the price of apple stock on day 3
# here O(n) = 1 # it directly picks the value using key

# for scenario 2 : on what day price was 103
# here O(n) = n # as it iterates through for loop till value is found

# for scenario 3 : print all prices
# here O(n) = n

# for scenario 4 : insert new price 312 at index 1
# here O(n) = n

# for scenario 5 :delete element at index 1
# here O(n) = n as after deleting element each element has to move up by 1 position
'''
Arrays are of 2 types
1. static arrays
2. Dynamic arrays
list is implemented as dynamic array in python
in java there is static Array
for static array initially fixed amount of contiguous memory location is allocated
then if we try to insert more elements than specified it throws error
in java dynamic array is implemented as Arraylist
here first a specific capacity say 10 is allocated in the memory,
after this gets filled , a new memory of 10 + (10 *2) gets allocated at
different location, so all the elements that already exists in memory get copied
to new memory location along with new data
Now when this gets filled again new memory is allocated with capacity : 30 + (30*2)

'''

'''
Arrays in python can handle heterogeneous data data
'''
# Exercise
'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
'''

expenses = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?

extra_expenditure = expenses[1] - expenses[0]
print(f"the amount spent extra in feb when compared to jan is : {extra_expenditure}")

#2. Find out your total expense in first quarter (first three months) of the year.

first_quarter_expense = sum(expenses[0:3])

print(f"first quarter expense is {first_quarter_expense}")

# 3. Find out if you spent exactly 2000 dollars in any month


print("2000 dollars are spent in any month?",2000 in expenses)
#4. June month just finished and your expense is 1980 dollar.
# Add this item to our monthly expense list

expenses.append(1980)
print(expenses)
# 5. You returned an item that you bought in a month of April and got a refund of 200$.
# Make a correction to your monthly expense list based on this
expenses[3] = expenses[3] - 200
print(expenses)

# problem 2

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list

print(f"length of list is {len(heros)}")
#2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
#3. You realize that you need to add 'black panther' after 'hulk',
#so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,"black panther")
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with
#     doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ["doctor strange"]
print(heros)
#. Sort the heros list in alphabetical order
# (Hint. Use dir() functions to list down all functions available in list)
print(dir(heros))
heros.sort()
print(heros)

# problem 3
# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

num = int(input("enter max number"))
lst = []
for i in range(1,num+1):
    if i % 2 !=0:
        lst.append(i)

print(lst)

