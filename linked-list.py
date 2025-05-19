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

    def dsply(self):
        if self.head is None:
            print("list is empty")
        else:
            current=self.head
            while current:
                print(current.data, end=" ,")
                current=current.next

sll=Single_linked_list()

while True:
    print("1.Insert at last\" \
         2.Insert in begining\
          3.Display\
          4. Exit")
    ch=int(input("enter choice: "))
    if ch==1:
        ele=int(input("enter element: "))
        sll.insertLast(ele)
    elif ch==2:
        ele=int(input("enter element: "))
        sll.insertBegin(ele)
    elif ch==3:
        sll.dsply()
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
'''