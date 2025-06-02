class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def preOrder(node):
    if node is None:
        return
    print(node.data,end=" ")
    preOrder(node.left)
    preOrder(node.right)

def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data,end=" ")

def inOrder(node):
    if node is None:
        return 
    inOrder(node.left)
    print(node.data,end=" ")
    inOrder(node.right)

def insert(root,data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root

nums = list(map(int, input().split()))
root=None
for num in nums:
    root=insert(root,num)
print("Enter operation you want to perform: ")
print("1.InOrder Traversal \n2.PreOrder Traversal \n3.PortOrder Traversal")
ch=int(input())
while ch:
    if ch==1:
        print(inOrder(root))
    elif ch==2:
        print(preOrder(root))
    elif ch==3:
        print(postOrder(root))
    else:
        print("Enter a valid choice! ")