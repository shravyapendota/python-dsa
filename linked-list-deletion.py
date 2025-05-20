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

    def insertAfter(self, value, after_val):
        newnode = Node(value)

        # Empty list check
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            if current.data == after_val:
                newnode.next = current.next
                current.next = newnode
                break
            current = current.next
        else:
            print(f"Node with value {after_val} not found.")
    

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
    print("1. Insert at Last\n2. Insert in Beginning\n3.Insert at a position\n4. Delete at Beginning\n5. \n Delete at End\n6. Display\n7.Search for ele\n8. Exit")

    ch=int(input("Enter choice: "))
    if ch==1:
        ele=int(input("Enter element: "))
        sll.insertLast(ele)
    elif ch==2:
        ele=int(input("Enter element: "))
        sll.insertBegin(ele)
    elif ch==3:
        ele=int(input("Enter number to insert "))
        pos=int(input("Enter postion to insert "))
        sll.insertPost(ele,pos)
    elif ch==4:
        ele=int(input("Enter number to insert "))
        pos=int(input("Enter postion to insert "))
        sll.insertPost(ele,pos)
    elif ch==5:
        sll.deleteFirst()
    elif ch==6:
        sll.deleteEnd()
    elif ch==7:
        sll.dsply()
    elif ch==8:
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

SEARCHING AN ELEMENT
STEP1: IF HEAD IS nONE
        PRINT "LIST IS EMPTY"
STEP2: ELSE:SET CURRENT=HEAD
STEP3:      WHILE CURRENT IS NOT NONe:
                IF CURRENT.DATA==SEARCH_ELEMENT THEN
                    PRINT " ELEMENT FOUND"
                END IF
                SET CURRENT=CURRENT.NEXT
            END WHILE
STEP4:PRINT "ELEMENT NOT FOUND"


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
