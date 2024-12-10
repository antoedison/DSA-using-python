#sll without returning head

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def insert_at_begining(self,data):
        curr = self.head
        new_node = Node(data)
        if curr is None:
            self.head = new_node
        new_node.next =curr
        self.head = new_node

    def insert_at_end(self,data):
        curr = self.head
        new_node = Node(data)
        if curr is None:
            self.head = new_node
            return
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_after(self,key,data):
        curr = self.head
        while curr:
            if curr.data is key:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
        print("key value not found")

    def insert_before(self,key,data):
        curr = self.head
        if curr.data == key:
            new_node = Node(data)
            new_node.next = curr
            self.head = new_node
            return
        while curr:
            if curr.next.data is key:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                return 
            curr = curr.next
        print("Key not found")

    def insert_at_index(self,position,data):
        curr = self.head
        if position == 1:
            new_node = Node(data)
            new_node.next = curr
            self.head = new_node
            return
        for _ in range(1,position-1):
            if curr.next == None:
                print("Index out of bounds")
                return
            curr = curr.next
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end= ' ')
            curr = curr.next

if __name__ == "__main__":

    linkedlist = LinkedList()

    while True:
        print("""
            Singly Linked List
            1. Insert at begining
            2. Insert at end
            3. Insert after
            4. Insert before
            5. Insert at index
            6. Display
            7. Exit
            """)
        choice = int(input("Enter the choice"))
        if choice == 1:
            print("Enter the data to be inserted at the begining")
            data = int(input())
            linkedlist.insert_at_begining(data)
        elif choice == 2:
            print("Enter the data to be inserted at the end")
            data = int(input())
            linkedlist.insert_at_end(data)
        elif choice == 3:
            key = int(input("Enter the key element"))
            data = int(input("Enter the element to be inserted after the key element"))
            linkedlist.insert_after(key,data)
        elif choice == 4:
            key = int(input("Enter the key element"))
            data = int(input("Enter the element to be inserted before the key element"))
            linkedlist.insert_before(key,data)
        elif choice == 5:
            position = int(input("Enter the position"))
            data = int(input("Enter the element"))
            linkedlist.insert_at_index(position,data)
        elif choice == 6:
            linkedlist.display()
        elif choice == 7:
            print("Exiting")
            break
        else:
            print("Invalid choice")
        
    
    




        
