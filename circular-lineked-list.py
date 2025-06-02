class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertLast(self, element):
        newnode = Node(element)
        if self.head is None:
            self.head = newnode
            newnode.next = newnode
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newnode
            newnode.next = self.head

    def insertBegin(self,element):
        newnode=Node(element)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            newnode.next=self.head
            current.next=newnode
            self.head=newnode

    def deleteBegin(self):
        if self.head is None:
            print("List is empty ")
        elif self.head.next==self.head:
            pritn(self.head.data,"Deleted List now empty")
            self.head=None
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            temp=self.head
            self.head=self.head.next
            current.next=self.head
            print(temp.data,"deleted")
            del temp


    def deleteLast(self):
        if self.head is None:
            print("List is empty ")
        elif self.head.next==self.head:
            print(self.head.data,"Deleted , list is now empty")
            self.head=None
        else:
            prev=None
            current=self.head
            while current.next!=self.head:
                prev=current
                current=current.next
            prev.next=self.head
            print(current.data,"Deleted")
            del current

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(None)
    
    
cll = CircularLinkedList()


cll.insertLast(1122)
cll.insertLast(2233)
cll.insertLast(3344)
cll.insertLast(4455)

print("Circular Linked List before insertion:")
cll.display()

element = int(input("Enter a value to insert at the end: "))
cll.insertLast(element)

print("Circular Linked List after insertion:")
cll.display()

cll.display()
element=int(input("Enter a value to insert at the begning : "))
cll.insertBegin(element)

print("Circular Linked List after insertion:")
cll.display()

cll.display()
cll.deleteBegin()
print("circular linkedlist after deleting the begning element ")
cll.display()
cll.display()
cll.deleteLast()
print("circular linkedlist after deleting the Last element ")
cll.display()


