class Queue : 
 
    def __init__(self) :
  
        self.items = []

    def isEmpty(self) :
       
        return len(self.items) == 0
    def enqueue(self, item) :
       
        self.items.append(item)
        print(f"Item {item} added to queue")

    def dequeue(self) :
       
        if self.isEmpty() :

            print("Queue is empty! Cannot dequeue.")
            return None
        
        return self.items.pop(0)
    
    def peek(self) :
 
        if self.isEmpty() :
     
            print("Queue is empty! Nothing to peek.")
            return None
        return self.items[0]
    
    def display(self) :

        print("Queue:", self.items)
        
# Driver code
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Front element:", q.peek())
print("Dequeued element:", q.dequeue())
q.display()
print("Is queue empty?", q.isEmpty())
