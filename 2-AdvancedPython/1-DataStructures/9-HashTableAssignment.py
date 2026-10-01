'''
nyc_weather.csv contains new york city weather for first few days in the
month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem
'''
temperatures = []
with open("nyc_weather.csv", 'r') as f:
        for line in f:
            tokens = line.split(',')
            temp = tokens[1].strip()
            if temp.isdigit():
                temperatures.append(int(temp))


print("the average temperatures for first week is : ",sum(temperatures[0:7])/7)

print("the max temperature in first 10 days is : ",max(temperatures[0:10]))

print("________________________")
'''
nyc_weather.csv contains new york city weather for first few days in 
the month of January. Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?
Figure out data structure that is best for this problem
'''
weather = {}
with open("nyc_weather.csv", 'r') as f:
        for line in f:
            tokens = line.split(',')
            temp = tokens[1].strip()
            if temp.isdigit():
                weather[tokens[0]] = int(temp)
print("the temperature on jan 9 is : ",weather['Jan 9'])
print("the temperature on jan 4 is : ",weather['Jan 4'])
print("________________________")
'''
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count as show below.
Think about the best data structure that you can use to solve this problem and 
figure out why you selected that specific data structure.
'''
word_count = {}
with open("poem.txt", 'r') as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            word = word.strip()
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word] = 1
print(word_count)
print("________________________")

'''
Implement hash table where collisions are handled using linear probing. 
We learnt about linear probing in the video tutorial. 
Take the hash table implementation that uses chaining and modify methods
to use linear probing.
Keep MAX size of arr in hashtable as 10.

'''

class HashMapProbing:
    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [[] for i in range(self.MAX_SIZE)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)  # ord function finds ASCII value of character
        return h % self.MAX_SIZE

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # checking if key already exists
        for element in self.arr:
            if len(element) >0:
                if element[0] == key:
                    element[1] = value
                    return

        if len(self.arr[h]) == 0 :
            self.arr[h]=[key,value]
            return
        slot_index = self.find_slot(h)
        if type(slot_index) is int:
            self.arr[slot_index] = [key, value]
        else:
            print(slot_index)

    def __getitem__(self, item):
        h = self.get_hash(item)

        index_range = self.get_probe_range(h)
        for i in index_range:
            if len(self.arr[i]) > 0:
                if self.arr[i][0] == item:
                    return self.arr[i][1]

        return "key is not found"

    def __delitem__(self, key):
        found = False
        h = self.get_hash(key)
        index_range = self.get_probe_range(h)
        for i in index_range:
            if len(self.arr[i]) > 0:
                if self.arr[i][0] == key:
                    self.arr[i] = []
                    found = True
                    break
        if not found:

            print("key is not found")






    # * converts the range into a list
    # + concatenates both the lists
    def get_probe_range(self,h):
        return [*range(h,self.MAX_SIZE)] + [*range(0,h)]


    def find_slot(self,h):
        for i in range(h, self.MAX_SIZE):
            if len(self.arr[i]) == 0:
                return i
        for j in range(h):
            if len(self.arr[j]) == 0:
                return j
        return "Slot not found and array is full"


t = HashMapProbing()
print(t.get_hash("march 6"))
print(t.get_hash("march 17"))
t.__setitem__("march 6",130)
t.__setitem__("march 17",140)
print(t.arr)
t.__setitem__("march 17",240)
print(t.arr)
print(t.get_hash("march 2"))
t.__setitem__("march 2",210)
print(t.arr)
print(t.__getitem__('march 17'))
print(t.__getitem__('march 2'))
print(t.__getitem__('march 5'))
t.__delitem__('march 17')
print(t.arr)
t.__delitem__('march 6')
print(t.arr)
t.__delitem__('march 5')
print(t.arr)


