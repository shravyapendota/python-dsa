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

    def nonPrime(self):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        temp = self.head
        pos = 1
        while temp is not None:
            if not is_prime(pos):
                print(temp.data)
            temp = temp.next
            pos += 1

                
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

# MENU-DRIVEN PROGRAM
sll = SingleLinkedList()

while True:
    print("\n--- Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert Before a Node")
    print("4. Insert After a Node")
    print("5. Delete from Beginning")
    print("6. Delete from End")
    print("7. Delete Before a Node")
    print("8. Delete After a Node")
    print("9. Display List")
    print("10. Display Nodes at Non-Prime Positions")
    print("11. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        ele = int(input("Enter element: "))
        sll.insertBegin(ele)

    elif ch == 2:
        ele = int(input("Enter element: "))
        sll.insertLast(ele)

    elif ch == 3:
        ele = int(input("Enter element to insert: "))
        key = int(input("Enter node before which to insert: "))
        sll.insertbeforeanode(ele, key)

    elif ch == 4:
        ele = int(input("Enter element to insert: "))
        key = int(input("Enter node after which to insert: "))
        sll.insertafteranode(ele, key)

    elif ch == 5:
        sll.deleteBegin()

    elif ch == 6:
        sll.deleteLast()

    elif ch == 7:
        key = int(input("Enter node before which to delete: "))
        sll.deleteBeforeNode(key)

    elif ch == 8:
        key = int(input("Enter node after which to delete: "))
        sll.deleteAfterNode(key)

    elif ch == 9:
        sll.display()

    elif ch == 10:
        print("Nodes at non-prime positions:")
        sll.nonPrime()

    elif ch == 11:
        print("Exit")
        break

    else:
        print("Invalid choice")
