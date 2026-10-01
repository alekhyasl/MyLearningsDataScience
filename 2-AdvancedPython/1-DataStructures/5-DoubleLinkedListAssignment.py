'''
Implement doubly linked list.
The only difference with regular linked list is that double linked has prev node
reference as well. That way you can iterate in forward and backward direction.
Your node class will look this this,
'''

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None # points to head of doublelinkedlist


    def insert_at_beginning(self,data):
        new_node = Node(data,self.head,None)
        self.head = new_node
        if self.head.next:
            itr = new_node.next
            itr.prev = new_node


    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data, self.head, None)
            self.head = new_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        new_node = Node(data,None,itr)
        itr.next = new_node

    def insert_values(self, data_list):
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

    def remove_element_at(self,index):
        if index < 0 or index >= self.get_length():
            print("not a valid index")
            return
        if index == 0:
            itr = self.head
            self.head = itr.next
            self.head.prev = None
            return
        itr = self.head
        count = 0
        while count < index - 1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next
        if index == (self.get_length()) - 1:
            itr.next.prev = itr

    def insert_element_at(self,index,data):
        if index < 0 or index >= self.get_length():
            print("not a valid index")
            return
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while count < index-1:
            itr = itr.next
            count += 1
        new_node = Node(data,itr.next,itr)
        itr.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        flag = False
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert,itr.next,itr)
                itr.next = new_node
                flag = True
                if new_node.next:
                    new_node.next.prev = new_node
            itr = itr.next
        try:

            if flag == False:
                raise Exception("the value to be inserted after data not found")
        except Exception as ex:
            print(ex)


    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            if self.head.next:
                self.head.next.prev = self.head
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
            if itr.next.next:
                itr.next = itr.next.next
                itr.next.prev = itr
            else:
                itr.next = None
        else:
            print("value to be removed not found")



    def display(self):
        if self.head is None:
            print("empty double linked list")
            return
        itr = self.head
        while itr:
            print(itr.data,end = '->')
            itr = itr.next
        print("None")

    def print_forward(self):
        if self.head == None:
            print("double linked list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data,end = '->')
            itr = itr.next
        print("None")



    def print_backward(self):
        if self.head is None:
            print("empty double linked list")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            print(itr.data,end= '->')
            itr = itr.prev
        print("None")


# Print linked list in reverse direction. Use node.prev for this.

if __name__ == "__main__":
    ll = DoubleLinkedList()
    ll.display()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(4)
    ll.display()
    ll.insert_at_end(7)
    ll.insert_at_end(9)
    ll.display()
    ll.insert_values(["apple", "mango", "banana", "cherry"])
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
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.display()
    ll.insert_after_value("mango", "kiwi")  # insert apple after mango
    ll.display()
    ll.insert_after_value("berry", "papaya")  # insert apple after mango
    ll.display()
    ll.insert_after_value("apple", "cherry")  # insert apple after mango
    ll.display()
    ll.remove_by_value("mango")
    ll.display()
    ll.remove_by_value("apple")
    ll.display()
    ll.remove_by_value("cherry")
    ll.display()
    ll.remove_by_value("pomo")
    ll.display()
    ll.insert_values(["apple", "mango", "banana", "cherry"])
    ll.print_forward()
    ll.print_backward()
