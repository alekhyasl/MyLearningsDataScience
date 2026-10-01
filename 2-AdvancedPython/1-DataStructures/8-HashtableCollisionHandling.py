# What is collision in hashMap?
# when the hash function is applied on key , if we get same value for more
# than one key in hashmap, this is called collision and this needs to be handled
# In order to prevent collision we store linked list instead of storing a single value
# in particular location
# so if we have second key have same value when hash function is applied that
# value is appended to the first element of linked list,
# here both key and value are stored in the linked list
# In this case the time complexity is O(n) for searching the element in the
# worst case scenario of bad hash function written
# Tha second way of handling collision is with probing
# suppose we have a key which gives same hash value as other key,
# so already a value is filled in that location, then it sees if next location
# is empty and keeps the value there

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)  # ord function finds ASCII value of character
        return h % self.MAX
    # adding key value pair to hash map
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        flag = False
        # to handle if the element already exist in linkedlist
        if len(self.arr[h]) > 0:
            for idx, element in enumerate(self.arr[h]):
                if element[0] == key:
                    self.arr[h][idx] = (key, value)
                    flag = True
                    break
        if flag == False:
            self.arr[h].append((key,value))
    # getting value
    def __getitem__(self, item):
        found = False
        h = self.get_hash(item)
        for element in self.arr[h]:
            if element[0] == item:
                found = True
                return element[1]
        if not found :
            return "element is not found"
    def __delitem__(self, key):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                found = True
                break
        if not found:
            print("element not found to delete")




t = HashTable()
print(t.get_hash("march 6"))
print(t.get_hash("march 17"))
t.__setitem__("march 6",130)
t.__setitem__("march 17",140)
print(t.arr)
t.__setitem__("march 17",240)
print(t.arr)
t.__setitem__("march 2",210)
print(t.arr)
print(t.__getitem__('march 17'))
print(t.__getitem__('march 2'))
print(t.__getitem__('march 5'))
t.__delitem__('march 17')
print(t.arr)
t.__delitem__('march 6')
print(t.arr)
