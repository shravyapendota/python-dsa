'''SIGLE LINKED LIST DELETION '''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
    
    def deleteFrisrt(head):
        if head is None:
            return None
        temp=head
        head=head.next
        del temp 
        return head
    
    def dsply(curr):
        while curr:
            print(curr,data,end=" ")
            curr=curr.nect
            