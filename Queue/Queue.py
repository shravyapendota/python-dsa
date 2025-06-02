class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, ele):
        self.queue.append(ele)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[0]

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue contents:", self.queue)


q = Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
q.enqueue(400)
q.display()       
print(q.dequeue())  
q.display()       
print(q.peek())     
