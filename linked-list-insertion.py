class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Single_linked_list:
    def __init__(self):
        self.head =None

    def insertLast(self,ele):
        newnode=Node(ele)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=newnode
        
    
    def insertBegin(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def deleteFirst(self):
        if self.head is None:
            print("List is empty")
        else:
            current=self.head
            self.head=current.next
            print(current.data,"Deleted")
            del current
            
    def deleteEnd(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            del self.head
            self.head = None
        else:
            second_last = self.head
            while second_last.next.next:
                second_last = second_last.next
            del second_last.next
            second_last.next = None

    def search(self, ele):
        if self.head is None:
            print("Element not found, list is empty")
            return False
        current = self.head
        while current:
            if current.data == ele:
                print("Element found!")
                return True
            current = current.next
        print("Element not found!")
        return False

    

    def dsply(self):
        if self.head is None:
            print("list is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next

sll=Single_linked_list()

while True:
    print("1. Insert at Last\n2. Insert in Beginning\n3. Delete at Beginning\n4. Delete at End\n5. Display\n6.Search for ele\n7. Exit")

    ch=int(input("Enter choice: "))
    if ch==1:
        ele=int(input("Enter element: "))
        sll.insertLast(ele)
    elif ch==2:
        ele=int(input("Enter element: "))
        sll.insertBegin(ele)
    elif ch==3:
        sll.deleteFirst()
    elif ch==4:
        sll.deleteEnd()
    elif ch==5:
        sll.dsply()
    elif ch==6:
        ele=int(input("Enter element to search for: "))
        sll.search(ele)
    else:
        break


'''
INSERT AT THE END
step1:create new node
step2: if head is Npne set head and poin tto newnode
step3:exit
step4:else
step5:set currentent=head
step6:repeat steps 7 while current.nect!=none
step7:update current to its next
step8:end of loop
step9:set surrent.next to the newnode
step10: Exit


    def deleteEnd(Self):  
        if self.head is None:
            print("list is empty")
        elif self.head.next==None:
            print(self.head.data,"deleted,empty list now")
            self.head=None
        else:
            prev=self.head
            current=self.head.next
            while current.next!=None:
                prev=current
                current=current.next
            print(current.data,"deleted")
            prev.next=None
'''
