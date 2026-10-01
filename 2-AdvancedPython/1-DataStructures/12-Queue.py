# Queue follows first in first out
'''
suppose we have New york stock exchange(NYSE) and Yahoo finance
One way of displaying stock prices in yahoo finance is with NYSE making a post call
to http server of yahoo finance
When the http server of yahoo finance is down then the stock prices sent during that
time are lost and there is no way to recieve the lost data after http server is up.
one more drawback using a post call to http server is suppose google finance
want to display stock prices from NYSE. Now NYSE team has to make code changes
to send data to google finance as the http url for google finance is different.
SO this is called tightly coupled system.
So in order to avoid the code changes everytime a new customer is onboared ,
NYSE uses Queue to send data , which is the memory buffer
The other way of displying stock prices in yahoo finance is using Queue to send
data to the consumer.
This is also called producer Consumer problem, here whatever is pushed inside first
comes out first. so called First in first out

In python we can use one the 3 approaches to create Queue
List
collections.deque
queue.lifoQueue
'''
from typing import Deque

# implementing Queue using list
walmart_stock_price = []
walmart_stock_price.insert(0,131)
walmart_stock_price.insert(0,135)
walmart_stock_price.insert(0,139)
walmart_stock_price.insert(0,134)
print(walmart_stock_price.pop())
print(walmart_stock_price.pop())
print(walmart_stock_price.pop())
print(walmart_stock_price.pop())

print("______________________________")

# implementing Queue using deque from collections

from collections import deque
q = deque()
q.appendleft(131)
q.appendleft(129)
q.appendleft(130)
q.appendleft(128)
q.appendleft(125)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

print("______________________________")

# implementing proper Queue class using python

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,data):
        self.buffer.appendleft(data)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})
print(pq.buffer)
print(pq.size())
print(pq.dequeue())
print(pq.dequeue())

'''
time complexity for insertion and deletion in Queue is O(1)
time complexity for search and accessing element is O(n)
'''