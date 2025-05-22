class Node:
    def __init__(self, prev, data, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

    def traverseBack(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.prev
        print("None")

    def insertBegin(self, ele):
        newnode = Node(None, ele, self.head)
        if self.head is not None:
            self.head.prev = newnode
        self.head = newnode

    def insertEnd(self,ele):
        newnode=Node(None,ele,None)
        if self.head==None:
            self.head=newnode
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp

    def insertAfter(self,ele,key):
        newnode=Node(None,ele,None)
        if self.head ==None:
            self.head=newnode
        temp=self.head
        while temp and temp.data!=key:
            temp=temp.next
        if temp==None:
            print("Node not found ")
        newnode.prev=temp
        newnode.next=temp.next
        if temp.next!=None:
            temp.next.prev=newnode
        temp.next=newnode

    def insertBefore(self,ele,key):
        newnode=Node(None,ele,None)
        if self.head==None:
            self.head=newnode
        temp=self.head
        while temp and temp.data!=key:
            temp=temp.next
        if temp==None:
            print("Node not found")
        newnode.next=temp
        newnode.prev=temp.prev
        if temp.prev!=None:
            temp.prev.next=newnode
        temp.prev=newnode

    def deleteBegin(self):
        if self.head==None:
            print("List is empty") 
        temp=self.head
        if self.head.next is None:
            self.head =None
            del temp
        self.head=self.head.next
        self.head.prev=None
        del temp
    
    def deleteEnd(self):

        if self.head==None:
            print("List is empty")
            return 
        temp=self.head
        if self.head.next is None:
            self.head=None
            del temp
        while temp.next!=None:
            temp=temp.next
        temp.prev.next=None
        del temp

    def deleteAfterVal(self,key):
        if self.head==None:
            print("List is empty ")
        temp=self.head
        while temp!=None and temp.data!= key:
            temp=temp.next
        if temp==None:
            print("Node not found")
        if temp.next==None:
            print("Node not found")
        delete=temp.next
        temp.next=delete.next
        if delete.next is None:
            delete.next.prev=temp
        del delete


# Pre-inserting nodes manually
n1 = Node(None, 10, None)
n2 = Node(n1, 20, None)
n3 = Node(n2, 30, None)
n4 = Node(n3, 40, None)

n1.next = n2
n2.next = n3
n3.next = n4

dll = DoubleLinkedList()
dll.head = n1

while True:
    print("\n1. Insert Begin\n2. Insert Last\n3.Insert before \n4. Insert after a node\n5. Delete begining\n6.Delete end \n8. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        ele = int(input("Enter the element to insert at beginning: "))
        dll.insertBegin(ele)
        dll.traverse()
    elif ch == 2:
        ele = int(input("Enter the element to insert at last: "))
        dll.insertEnd(ele)
        dll.traverse()
    elif ch == 3:
        ele = int(input("Enter the element to insert: "))
        key = int(input("Enter the node before which to insert: "))
        dll.insertBefore(ele, key)
        dll.traverse()
    elif ch == 4:
        ele = int(input("Enter the element to insert: "))
        key = int(input("Enter the node after which to insert: "))
        dll.insertAfter(ele, key)
        dll.traverse()
    elif ch==5:
        dll.deleteBegin()
        dll.traverse()
    elif ch==6:
        dll.deleteEnd()
        dll.traverse()
    elif ch==7:
        key=int(input("Enter a elemnt to delete after "))
        dll.deleteAfterVal(key)
        dll.traverse()
    elif ch == 8:
        break
    else:
        print("Invalid choice, try again.")
