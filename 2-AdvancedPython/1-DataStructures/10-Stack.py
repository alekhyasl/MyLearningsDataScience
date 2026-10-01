# Stack
# Stack follows last in first out
# suppose you open the browser and navigate to website , where u click on various
# links.Now when you click on back button . you navigate to the page which you
# clicked last. So this follows last in first out
# In stack pushing/poping element is order of 1 -> O(1)
# In stack searching for element is order of n -> O(n)
# Function calling in any programming language is managed using stack
# the initially called function is pushed to last
# the undo operation in word, the last operation performed is removed first
# in python stack is implemented using list, collections.deque,queue.LifoQueue

stack = []
stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/world/india")
stack.append("https://www.cnn.com/world/australia")
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
#print(stack.pop()) # cannot pop from empty list
# suppose you do not want to remove an element from the list, but just to get the data
# we can use negative index to retrieve last element
stack1 = [1,2,3,4,5]
print(stack1[-1])
# the drawback of using the list for implementing stack is
# initially list has a capacity say 10, when the capacity is full ,and we try to
# insert new elements all the existing elements are moved to new memory creating more
# space for new elements,which can increase the complexity of program
# So instead of list we can use collections.deque to implement stack
# deque os not a linked list. It is a linked list of fixed‑size arrays (blocks)

from collections import deque
stack = deque()
print(dir(stack))
stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/world/india")
stack.append("https://www.cnn.com/world/australia")
stack.pop()
print(stack)

# stack implementation in python

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
s.push(4)
print(s.pop())
print(s.peek())
print(s.size())
print(s.pop())
print(s.is_empty())



