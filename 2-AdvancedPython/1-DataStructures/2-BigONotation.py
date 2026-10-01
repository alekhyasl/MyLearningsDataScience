# Big O Notation -> is used to measure how the running time or space
# requirements of the program grows as input size grows
from debugpy.common.sockets import serve


def foo(arr):
    pass
# time taken for this function when size(arr) = 100 -> 0.22 millisecond
# time taken for this function when size(arr) = 1000 ->2.30 millisecond
# this indicates the time increases linearly with size of array
# time = an +b -> we keep the fastest growing term and ignore constants
# here fastest growing term is an
# the time complexity is O(n)

# Example
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers
# here time complexity is O(n) as input increase time increases linearly

# Example

def find_pe(prices,eps,index):
    pe = prices[index]/eps[index]
    return pe
# here time complexity is O(1) as processing time is same
# irrespective of length of price and eps

# Example
numbers = [3,6,2,3,4,5,6]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break

# here we have n^2 iterations
# so O(n) = n^2

numbers = [3,6,2,3,4,5,6]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break
for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)

# here number of iterations = an^2 + bn +b
# 1.here we keep fastest growing term which is n^2 here
# 2.drop constants
# O(n) = n^2

# Till now we saw time complexity(time growth wrt input)
# there is space complexity which is similar to time complexity

# Example of binary serach
# say we have sorted list of numbers
# 4 9 15 21 34 57 68 91  , serach for 68

lst = [4,9,15,21,34,57,68,91]
search = 68
for i in lst:
    if  i == search:
        print(i)

# for this time complexity is O(n)
# lets take the approach of binary search
# 4 9 15 21 | 34 57 68 91
# take middle elements say 21 compare with 68 which is greater than 21
# Now compare with the middle element in the right half
#34 57 68 91
# here 57 is the middle element here 57 < 68
# again compare with the middle element in the right half
# 68 91 Now 68 is the search element
# here number is found in 3 iterations

# iteration 1 : n/2
# iteration 2 : (n/2)/2 = n/4
# iteration 3  : n/8

# iteration k  : n/(2^k)

# 1 = n/(2^k)
# 2^k = n
# log 2^k = log n
#k = log n
# O(n) = log n
# log(8) = log 2^3 = 3













