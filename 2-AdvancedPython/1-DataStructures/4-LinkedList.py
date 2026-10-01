# Linked list
# Advantages of linked list over arrays
'''
we have stock_price = [101,103,99,111,119]
In order to insert value 105 say at location 1 , in stock_price
case 1: if the allocated capacity is not full in the list, say capacity = 10
in order to insert new value at location 1,it has to move the elements from
location 1 to 4 to the next location
so O(n) = n
case 2 : if the allocated capacity of list is full
in this case we have to move the new and existing elements to the new memory
location
'''
# unlike arrays storing values in contiguous memory locations
# linked list stores value in random memory locations, which are linked by pointers
# so first element has reference to second element , second has reference to third etc
# 298 | 0x00A1 -> 305 | 0x00C1 -> 312 | 0x01A1 -> 301 | 0x00D2
#               0x00A1            0x00C1          0x01A1
'''
here if we want to insert element at position 1
the reference of element at position 0 needs to be updated , to the new element 
memory location ,the new elements keeps the reference of next element
so here O(n) = 1
So the 2 benefits in linked list is
1. no need to pre allocate space
2. Insertion is easier
'''
'''
Double linked list
with the help of double linked list we can traverse back and fourth
each element contains address of before and after element

'''
# impelentation of linked list

class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None # points to head of linkedlist

    def insert_at_beginning(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        new_node = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # remove an element at specific index
    def remove_element_at(self,index):
        if index < 0 or index >= self.get_length():
            print("not a valid index")
            return
        if index == 0:

            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while count < index - 1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def insert_element_at(self,index,data):
        if index < 0 or index >= self.get_length():
            print("not a valid index")
            return
        if index == 0:
            itr = self.head
            self.head = Node(data,itr)
            return
        itr = self.head
        count = 0
        while count < index-1:
            itr = itr.next
            count += 1
        new_node = Node(data,itr.next)
        itr.next = new_node

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        flag = False
        while itr:
            if itr.data == data_after:
                flag = True
                break
            itr = itr.next
        if flag:
            new_node = Node(data_to_insert,itr.next)
            itr.next = new_node
        else:
             print("data is not found to insert")



    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        flag = False
        while itr:
            if itr.next:
                if itr.next.data == data:
                    flag = True
                    break
            itr = itr.next
        if flag:
            itr.next = itr.next.next
        else:
            print("value to be removed not found")







    def display(self):
        if self.head is None:
            print("empty linked list")
            return
        itr = self.head
        while itr:
            print(itr.data,end = '->' )
            itr = itr.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.display()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(4)
    ll.display()
    ll.insert_at_end(7)
    ll.insert_at_end(9)
    ll.display()
    ll.insert_values(["apple","mango","banana","cherry"])
    ll.display()
    print(ll.get_length())
    ll.remove_element_at(0)
    ll.display()
    ll.remove_element_at(3)
    ll.display()
    ll.remove_element_at(1)
    ll.display()
    ll.remove_element_at(1)
    ll.display()
    ll.insert_element_at(1,"blue berry")
    ll.display()
    ll.insert_element_at(8, "strawberry")
    ll.display()
    ll.insert_element_at(0, "strawberry")
    ll.display()
    ll.insert_element_at(2, "guvava")
    ll.display()
    ll.insert_after_value("mango","orange")
    ll.display()
    ll.insert_after_value("black berry", "orange")
    ll.display()
    ll.insert_after_value("cherry", "kiwi")
    ll.display()
    ll.remove_by_value("mango")
    ll.display()
    ll.remove_by_value("strawberry")
    ll.display()
    ll.remove_by_value("kiwi")
    ll.display()
    ll.remove_by_value("pomo")
    ll.display()
    print("_______________________")
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.display()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.display()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.display()
    ll.remove_by_value("figs")
    ll.display()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.display()





