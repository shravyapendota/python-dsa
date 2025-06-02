class Node:
    def __init__(self, element): 
        self.data = element
        self.next = None

class SingleLinkedList():
    def __init__(self):  
        self.head = None

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverseList(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head = prev 

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next
            print("None")

linked_list = SingleLinkedList()
for value in [10, 20, 30, 40, 50]:
    linked_list.append(value)

linked_list.display()
linked_list.reverseList()
linked_list.display()
