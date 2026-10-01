'''
Write a function in python that can reverse a string using stack data structure.
Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
'''
from collections import deque
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

def reverse_string(data):
    reverse_string = Stack()
    rstr = ""
    for ch in data:
        reverse_string.push(ch)
    while reverse_string.size() != 0:
        rstr += reverse_string.pop()
    return rstr

'''
Write a function in python that checks if paranthesis in the string are 
balanced or not. Possible parantheses are "{}',"()" or "[]". 
Use Stack class from the tutorial.
'''

def match_func(key):
    match_dict = {
         '}' : '{',
        ']' :'[',
        ')' : '('
    }
    return match_dict[key]

def is_paranthesis_balanced(data):
    s = Stack()

    for ch in data:
        if ch == '[' or ch == '{' or ch == '(':
            s.push(ch)
        if ch == ']' or ch == '}' or ch == ')':
            if s.size() == 0:
                return False
            if not (s.pop() == match_func(ch)):
                return False
    return s.size() == 0





if __name__ == "__main__":
    print(reverse_string("We will conquere COVID-19"))
    print(is_paranthesis_balanced("({a+b})"))
    print(is_paranthesis_balanced("))((a+b}{"))
    print(is_paranthesis_balanced("((a+b))"))
    print(is_paranthesis_balanced("))"))
    print(is_paranthesis_balanced("[a+b]*(x+2y)*{gg+kk}"))

