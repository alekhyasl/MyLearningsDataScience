# Implementing hash map
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)  # ord function finds ASCII value of character
        return h % self.MAX
    # adding key value pair to hash map
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h]=value
    # getting value
    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t['march-06'] = 123
t['march-07'] = 124
t['march-09'] = 125
t['march-19'] = 120
t['march-20'] = 130
print(t['march-06'])
print(t['march-09'])
print(t['march-07'])
print(t.arr)
del t['march-06']
print(t.arr)
