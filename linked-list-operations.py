class Node:
    def __init__(self, element): 
        self.data = element
        self.next = None

class SingleLinkedList():
    def __init__(self):  
        self.head = None

    def insertBegin(self, ele):
        newnode = Node(ele)
        newnode.next = self.head
        self.head = newnode

    def insertLast(self, ele):
        newnode = Node(ele)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode

    def insertbeforeanode(self, ele, key):
        newnode = Node(ele)
        if self.head is None:
            print("Linked list is empty, insertion not possible")
        elif self.head.data == key:
            newnode.next = self.head
            self.head = newnode
        else:
            prev = None
            current = self.head
            while current and current.data != key:
                prev = current
                current = current.next
            if current:
                prev.next = newnode
                newnode.next = current
            else:
                print("Node with data", key, "not found")

    def insertafteranode(self, ele, key):
        newnode = Node(ele)
        current = self.head
        while current:
            if current.data == key:
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
        print("Node with data", key, "not found")

    def deleteBegin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            self.head = self.head.next
            print(temp.data, "deleted")
            del temp

    def deleteLast(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.next is None:
            print(self.head.data, "deleted")
            self.head = None
        else:
            prev = self.head
            current = self.head.next
            while current.next:
                prev = current
                current = current.next
            print(current.data, "deleted")
            prev.next = None

    def deleteBeforeNode(self, key):
        if self.head is None or self.head.next is None:
            print("Not enough elements to delete before node.")
            return

        # Special case: head is before the key
        if self.head.next.data == key:
            temp = self.head
            self.head = self.head.next
            print(temp.data, "deleted (before", key, ")")
            del temp
            return

        # General case
        prev = self.head
        current = prev.next
        while current.next and current.next.data != key:
            prev = current
            current = current.next

        if current.next and current.next.data == key:
            print(current.data, "deleted (before", key, ")")
            prev.next = current.next
            del current
        else:
            print("Node with data", key, "not found or no node before it.")

    def deleteAfterNode(self, key):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current and current.data != key:
            current = current.next

        if current is None:
            print("Node with data", key, "not found.")
        elif current.next is None:
            print("No node exists after", key, "to delete.")
        else:
            temp = current.next
            current.next = temp.next
            print(temp.data, "deleted (after", key, ")")
            del temp

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# Menu-driven program
sll = SingleLinkedList()
while True:
    print("\n1. Insert@Begin\n2. Insert@Last\n3. Delete@Begin\n4. Delete@Last\n5. Insert before a node\n6. Insert after a node\n7. Display\n8. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        ele = int(input("Enter the element to insert at beginning: "))
        sll.insertBegin(ele)
    elif ch == 2:
        ele = int(input("Enter the element to insert at last: "))
        sll.insertLast(ele)
    elif ch == 3:
        ele = int(input("Enter the element to insert: "))
        key = int(input("Enter the node before which to insert: "))
        sll.insertbeforeanode(ele, key)
    elif ch == 4:
        ele = int(input("Enter the element to insert: "))
        key = int(input("Enter the node after which to insert: "))
        sll.insertafteranode(ele, key)
    elif ch == 5:
        sll.deleteBegin()
    elif ch == 6:
        sll.deleteLast()
    elif ch==7:
        sll.deleteBeforeNode()
    elif ch==8:
        sll.deleteBeforeNode
    elif ch == 7:
        sll.display()
    elif ch == 8:
        break
    else:
        print("Invalid choice, try again.")
