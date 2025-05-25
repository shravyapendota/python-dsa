def findTheWinner(n,k):
    lst=[i+1 for i in range(n)]
    index=0
    while len(lst)>1:
        index=(index+k-1)%len(lst)
        lst.pop(index)
    return lst[0]

n=int(input())
k=int(input())
print(findTheWinner(n,k))
