class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(105)
n2=Node(106)
n3=Node(107)
n1.next=n2
n2.next=n3

curr=n1
while curr:
    print(curr.data)
    curr=curr.next