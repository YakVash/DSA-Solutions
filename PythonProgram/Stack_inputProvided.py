#Program to implement stack when inputs are provided
class Stack :
 
    def __init__(self) :

        self.items = []
        
    def isEmpty(self) :
       
        return len(self.items) == 0
    
    def push(self, item) :
       
        self.items.append(item)
        print(f"Item {item} pushed onto stack")

    def pop(self) :
 
        if self.isEmpty() :

            print("Stack is empty! Cannot pop.")
            return None
        
        return self.items.pop()
    
    def peek(self) :
 
        if self.isEmpty() :
     
            print("Stack is empty! Nothing to peek.")
            return None
        
        return self.items[-1]
    
    def display(self) :
 
        print("Stack:", self.items)

# Driver code
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top element:", s.peek())
print("Popped element:", s.pop())
s.display()
print("Is stack empty?", s.isEmpty())