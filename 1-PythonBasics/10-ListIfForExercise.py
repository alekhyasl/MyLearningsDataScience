### Task 1
# 1. You are a Marvel fan and created a list of superheroes.
# Using this list, calculate how many members in the Avengers team?
print("---------Task1-----------")
avengers  = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
print(len(avengers))

print("---------Task2-----------")

### Task 2
# Awesome. Now Iron Man made Spider-Man a new member of the Avengers,
# add him to your list at the end
avengers.append('Spider-Man')
print(avengers)

print("---------Task3-----------")

### Task 3

# Looks like you are loving this avengers exercise already😄,
# Let's add a twist to it. Everyone came to a conclusion that Captain America is the '
#  'leader of the Avengers, so please add him before the Iron Man.
#  Hint: You can first remove him from the list and add before the Iron Man.
#  To remove him you can use a method called .pop())
# Feel free to take help of ChatGPT just in case you are confused about pop() method.
# Remember becoming a good Python programmer is all about how well you can
# learn new things on your own

avengers.pop(1) # pop function works without index, with index, with negative index
avengers.insert(0,'Captain America')
print(avengers)

print("---------Task4-----------")

# Thor and Hulk are getting angry easily and fight with each other.
# So you have to separate them with each other.
# To separate them, move “Black Widow” in between them.
print(avengers)
avengers.insert(4,avengers[2])
avengers.remove("Black Widow")
print(avengers)

print("---------Task5-----------")
# Below list contains scores of students in a class as per their roll number.
# Which means the first element is for roll # 1, second one is for roll # 2 and so on.
# # Print the scores of,
#
# 1. The first student
# 1. The last student
# 1. First 3 students
# 1. Scores of roll # 3, 4 and 5

scores = [92, 85, 76, 58, 89, 91, 73, 84]
print(f"score of first student is {scores[0]}")
print(f"score of last student is {scores[-1]}")
print(f"score of first 3 students is {scores[:3]}")
print(f"score of 3,4,5 student is {scores[2:5]}")

print("---------Task6-----------")
### Task 6
#
# We got a result of one more student which is 83 marks.
# Append this to the ```scores``` at the end and print the list
scores.append(83)
print(scores)


### Task 7

# Categorizes each score into a grade based on the following thresholds:
#
# 1. A: 90 to 100
# 1. B: 80 to 89
# 1. C: 70 to 79
# 1. D: 60 to 69
# 1. F: Below 60
#
# Count the number of students in each grade category and print the summary of how many students received each grade.
#
# Expected output
#
# ```
# Grade Summary:
# - A: 2 students
# - B: 4 students
# - C: 2 students
# - D: 0 students
# - F: 1 students
# ```
print("---------Task7-----------")

a_count,b_count,c_count,d_count,f_count = 0,0,0,0,0
for score in scores:
    if score <= 100 and score >= 90:
        a_count += 1
    elif score <= 89 and score >= 80:
        b_count += 1
    elif score <= 79 and score >= 70:
        c_count += 1
    elif score <= 69 and score >= 60:
        d_count += 1
    else:
        f_count += 1

print("Grade Summary :")
print(f"- A: {a_count} students")
print(f"- B: {b_count} students")
print(f"- C: {c_count} students")
print(f"- D: {d_count} students")
print(f"- F: {f_count} students")

### Task 8
#
# Managing inventory efficiently is crucial for businesses to
# ensure they do not run out of key products.
# This exercise simulates a simple inventory management system where the user can see
# which items are below the minimum stock level and need reordering.
# Below you have two lists that stores product names and their inventory stock levels.
# Using that,
#
# 1. Check each item to see if its stock level is below a minimum threshold.
# 1. If the stock level is below the minimum, add the product's name to a reorder list.
# 1. Print a list of products that need to be reordered.
#
# Expected Output
# ```
# Items to Reorder:
# - Pears
# - Grapes
# ```

# Lists to store product names and stock levels
print("---------Task8-----------")
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering
reorder_list = []
print("Items to Reorder:")
for product_name,stock_level in zip(product_names,stock_levels):
    if stock_level<10:
        reorder_list.append(product_name)

for reorder_item in reorder_list:
        print(f"- {reorder_item}")

