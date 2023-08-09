# This Program will contain linked list Implementation of singly linked list and its various functions:


# Node Class
class Node:
    def __init__ (self, data = None, next = None):
        self.data = data
        self.next = next
        
# Linked list Class
class LinkedList:

    def __init__(self):
        self.head = None
        
    # Function to insert the data at begin
    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node
        
    # Function to display the data
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llistr = ''

        while itr!= None:
            llistr += str(itr.data) +'-->'
            itr=itr.next

        print(llistr)
        
    # Function to insert data at end
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next!=None:
            itr = itr.next

        itr.next = Node(data, None)

    # Function to insert a list of elements
    def insert_list_of_values(self, data_list):
        #self.head = None # using this to clean the
        #existing linked list and reading the
        #data, but if we dont use this,
        #we can add data to existing linked list
        
        for data in data_list:
            self.insert_at_end(data)
            #self.insert_at_begin(data)

    # Function to get length of linkedList
    def get_len(self):
        count = 0
        itr = self.head
        while itr!=None:
            count+=1
            itr = itr.next
        return count

    # Function to remove nodes:
    def remove_at(self, index):
        if index < 0 and index > self.get_len():
            raise Exception("Invalid Index, Please give an index greater thn equal to 0 and smaller thn length of list")

        if index == 0:
            self.head == self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    # Funcion to insert at given index:
    def insert_at(self, data, index):
        if index < 0 and index > self.get_len():
            raise Exception("Invalid Index, Please give an index greater thn equal to 0 and smaller thn length of list")

        if index == 0:
            self.insert_at_begin(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1
            
           
# Main Function         
if __name__ == '__main__':

    l1 = LinkedList()
    l1.insert_at_begin(5)
    l1.insert_at_end(20)
    l1.insert_list_of_values(['heloo','Okay', 'Bye'])
    #l1.insert_list_of_values(['heyyyoooo','coolio', 'I like beach weather']) #at start
    lent = l1.get_len()
    print('Length of linked list: ', lent)
    l1.display()
    l1.remove_at(1)
    print('List after removing data: ', end = '')
    l1.display()
    l1.insert_at("data", 2)
    print('List after inserting data: ', end = '')
    l1.display()
    
            
        
